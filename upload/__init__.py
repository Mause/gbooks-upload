#!/usr/bin/env python3

import logging
import time
from mimetypes import add_type
from typing import Callable, Optional

import httplib2
import rich_click as click
from googleapiclient.discovery import Resource, build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

from .const import COOKIE_TXT, PATH
from .drive import upload_with_drive
from .scotty import steal_cookie, upload_with_scotty

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
    cookie = steal_cookie(filename)
    if not cookie:
        raise Exception("Could not find cookie")
    PATH.mkdir(parents=True, exist_ok=True)
    COOKIE_TXT.write_text(cookie)


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
