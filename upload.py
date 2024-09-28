#!/usr/bin/env python3

import argparse
import logging
import os.path
import re
import time
from mimetypes import add_type, guess_type
from typing import Callable

import dotenv
import httplib2
import requests
from googleapiclient.discovery import Resource, build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from typing import Optional

dotenv.load_dotenv()

logging.basicConfig(level=logging.DEBUG)
add_type("application/epub+zip", ".epub")
LNCR = re.compile(r"^(?P<title>.*) c(?P<start>\d+)-(?P<end>\d+)$")
assert LNCR.search("Season Of Fools c1-2")


# for service in ["books_v1", "drive_v3"]:
#     filename = service + ".json"
#     if not exists(filename):
#         url = "https://www.googleapis.com/discovery/v1/apis/{}/{}/rest".format(
#             *service.split("_")
#         )
#         with open(filename, "wb") as fh:
#             fh.write(requests.get(url).content)


def get_http():
    args = argparser.parse_args(["--noauth_local_webserver"])
    flow = flow_from_clientsecrets(
        "client_secrets.json",
        scope=[
            "https://www.googleapis.com/auth/drive.file",
            "openid",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/books",
        ],
    )
    storage = Storage("credentials.json")
    credentials = storage.get()
    if credentials is None:
        credentials = run_flow(flags=args, flow=flow, storage=storage)
    http = credentials.authorize(httplib2.Http())
    if credentials.access_token_expired:
        credentials.refresh(http)
    return http


def upload(drive, books, filename):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    http = get_http()

    books = build("books", "v1", http=http)
    drive = build("drive", "v3", http=http)

    uploads = [upload(drive, books, filename) for filename in args.files]
    for upl in uploads:
        monitor(books, upl["volumeId"])


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
            "cookie": os.environ["COOKIE"],
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


if __name__ == "__main__":
    main()
