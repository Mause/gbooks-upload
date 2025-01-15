import os
from mimetypes import guess_type

import requests
from googleapiclient.discovery import Resource

from .const import COOKIE_TXT


def steal_cookie(data: dict) -> str | None:
    events = data["events"]
    events = [event["params"] for event in events if event["type"] == 201]

    for event in events:
        headers = event["headers"]
        headers = dict(header.split(": ", 1) for header in headers)

        authority = headers.get(":authority")
        if authority and "playbooks" in authority:
            return headers["cookie"]
    return None


def upload_with_scotty(books: Resource, filename: str) -> dict:
    content_id = resume_upload(filename)

    return (
        books.cloudloading()
        .addBook(
            upload_client_token=content_id,
        )
        .execute()
    )


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
