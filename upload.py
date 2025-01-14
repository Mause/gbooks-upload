#!/usr/bin/env python3

import json
import logging
import os.path
import time
from mimetypes import add_type, guess_type
from os.path import basename, splitext
from pathlib import Path
from typing import Callable, Optional

import httplib2
import requests
import rich_click as click
from googleapiclient.discovery import Resource, build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from platformdirs import user_cache_dir

PATH = Path(user_cache_dir("gbooks-upload", "Elliana May"))
COOKIE_TXT = PATH / "cookie.txt"

add_type("application/epub+zip", ".epub")


def get_http():
    assert argparser
    args = argparser.parse_args(["--noauth_local_webserver"])
    flow = flow_from_clientsecrets(
        PATH / "client_secrets.json",
        scope=[
            "https://www.googleapis.com/auth/drive.file",
            "openid",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/books",
        ],
    )
    storage = Storage(PATH / "credentials.json")
    credentials = storage.get()
    if credentials is None:
        credentials = run_flow(flags=args, flow=flow, storage=storage)
    http = credentials.authorize(httplib2.Http())
    if credentials.access_token_expired:
        credentials.refresh(http)
    return http


def upload_with_drive(drive: Resource, books: Resource, filename: str) -> dict:
    name = splitext(basename(filename))[0]
    mime_type = guess_type(filename)[0]
    response = (
        drive.files().create(media_body=filename, media_mime_type=mime_type).execute()
    )

    return (
        books.cloudloading()
        .addBook(
            # A drive document id. The upload_client_token must not be set.
            drive_document_id=response["id"],
            # The document MIME type.
            # It can be set only if the drive_document_id is set.
            mime_type=mime_type,
            # The document name.
            # It can be set only if the drive_document_id is set.
            name=name,
        )
        .execute()
    )


def upload_with_scotty(books: Resource, filename: str) -> dict:
    content_id = resume_upload(filename)

    return (
        books.cloudloading()
        .addBook(
            upload_client_token=content_id,
        )
        .execute()
    )


def get_volume(
    books: Resource, name: Optional[str] = None, volumeId: Optional[str] = None
):
    return next(
        volume
        for volume in books.volumes().useruploaded().list().execute()["items"]
        if (volume["volumeInfo"]["title"] == name or volume["id"] == volumeId)
    )


def paginate(method: Callable, *args, **kwargs):
    request = method(*args, **kwargs)
    start_index = 0
    while request:
        res = request.execute()
        if "items" not in res:
            break
        yield from res["items"]
        start_index += len(res["items"])
        request = method(*args, startIndex=start_index, **kwargs)


@click.group()
@click.option("--verbose", is_flag=True)
def main(verbose: bool) -> None:
    if verbose:
        logging.basicConfig(level=logging.DEBUG)


@main.command()
@click.argument(
    "files", required=True, nargs=-1, type=click.Path(exists=True, readable=True)
)
@click.option("--use-drive", is_flag=True)
@click.option("--bookshelf")
def upload(files: list[str], use_drive: bool, bookshelf: str):
    """
    Upload files to Google Books
    """

    http = get_http()

    books = build("books", "v1", http=http)
    drive = build("drive", "v3", http=http)

    uploads = [
        upload_with_drive(drive, books, filename)
        if use_drive
        else upload_with_scotty(books, filename)
        for filename in files
    ]
    for upl in uploads:
        monitor(books, upl["volumeId"])


@main.command()
@click.argument("filename", type=click.Path(exists=True, readable=True))
def steal(filename: str):
    """
    Steal the cookie from a Chrome net-export log
    """
    COOKIE_TXT.write_text(steal_cookie(filename))


def start_upload(session: requests.Session, filename: str, mimetype: str):
    stat = os.stat(filename)
    filesize = stat.st_size
    title = os.path.basename(filename)

    res = session.post(
        "https://docs.google.com/upload/books/library/upload",
        params={"authuser": "0", "opi": "113040485"},
        headers={
            "accept": "*/*",
            # "content-length": "557",
            "origin": "https://docs.google.com",
            "priority": "u=1, i",
            "referer": "https://docs.google.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-goog-upload-command": "start",
            "x-goog-upload-header-content-length": str(filesize),
            "x-goog-upload-header-content-type": mimetype,
            "x-goog-upload-protocol": "resumable",
        },
        json={
            "protocolVersion": "0.8",
            "createSessionRequest": {
                "fields": [
                    {
                        "external": {
                            "name": "file",
                            "filename": title,
                            "put": {},
                            "size": filesize,
                        }
                    },
                    {
                        "inlined": {
                            "name": "title",
                            "content": title,
                            "contentType": "text/plain",
                        }
                    },
                    {
                        "inlined": {
                            "name": "addtime",
                            "content":
                            # int(stat.st_atime * 1000),
                            "1723462164781",
                            "contentType": "text/plain",
                        }
                    },
                    {
                        "inlined": {
                            "name": "onepick_version",
                            "content": "v2",
                            "contentType": "text/plain",
                        }
                    },
                    {
                        "inlined": {
                            "name": "onepick_host_id",
                            "content": "20",
                            "contentType": "text/plain",
                        }
                    },
                    {
                        "inlined": {
                            "name": "onepick_host_usecase",
                            "content": "PlayBooks.Web",
                            "contentType": "text/plain",
                        }
                    },
                ]
            },
        },
    )
    """
    X-Goog-Upload-Chunk-Granularity:
    262144
    X-Goog-Upload-Control-Url:
    https://docs.google.com/upload/books/library/upload?authuser=0&opi=113040485&upload_id=AHxI1nMkzatj-c5HRv1gmlu1-AME4SLqMPzCKrBPPvMJJtcDHtbrY-MyVI9q84dRBRG-GStp0MKj_bhLYiXyvfPlHGpWKQdaKJeKqPtHutcsL8Qc-Q&upload_protocol=resumable
    X-Goog-Upload-Status:
    active
    X-Goog-Upload-Url:
    https://docs.google.com/upload/books/library/upload?authuser=0&opi=113040485&upload_id=AHxI1nMkzatj-c5HRv1gmlu1-AME4SLqMPzCKrBPPvMJJtcDHtbrY-MyVI9q84dRBRG-GStp0MKj_bhLYiXyvfPlHGpWKQdaKJeKqPtHutcsL8Qc-Q&upload_protocol=resumable
    X-Guploader-Uploadid:
    AHxI1nMkzatj-c5HRv1gmlu1-AME4SLqMPzCKrBPPvMJJtcDHtbrY-MyVI9q84dRBRG-GStp0MKj_bhLYiXyvfPlHGpWKQdaKJeKqPtHutcsL8Qc-Q
    """
    if not res.ok or "x-goog-upload-url" not in res.headers:
        raise Exception(res.text)

    return res.headers["X-Goog-Upload-Url"]


def resume_upload(filename):
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            "cookie": COOKIE_TXT.read_text(),
        }
    )

    mimetype = guess_type(filename)[0]
    if not mimetype:
        raise Exception(f"Could not determine mimetype for {filename}")

    url = start_upload(session, filename, mimetype)

    res = session.put(
        url,
        headers={
            "accept": "*/*",
            "content-type": mimetype,
            "origin": "https://docs.google.com",
            "priority": "u=1, i",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-goog-upload-command": "upload, finalize",
            "x-goog-upload-offset": "0",
            "referer": "https://docs.google.com/",
        },
        data=open(filename, "rb").read(),
    )

    js = res.json()
    if "errorMessage" in js:
        raise Exception(js["errorMessage"])

    completion_info = js["sessionStatus"]["additionalInfo"][
        "uploader_service.GoogleRupioAdditionalInfo"
    ]["completionInfo"]

    assert completion_info["status"] == "SUCCESS"

    return completion_info["customerSpecificInfo"]["contentId"]


def monitor(books: Resource, volume_id: str) -> None:
    wait = 1

    while True:
        state = get_volume(books, volumeId=volume_id)["userInfo"][
            "userUploadedVolumeInfo"
        ]["processingState"]
        print(state)
        if state.startswith("COMPLETED_"):
            break
        time.sleep(wait)
        wait *= 1.5


def steal_cookie(filename):
    with open(filename) as f:
        events = json.load(f)["events"]
    events = [event["params"] for event in events if event["type"] == 201]

    for event in events:
        headers = event["headers"]
        headers = dict(header.split(": ", 1) for header in headers)

        if "playbooks" in headers[":host:"]:
            return headers["cookie"]
    return None


if __name__ == "__main__":
    main()
