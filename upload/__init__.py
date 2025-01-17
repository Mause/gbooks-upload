#!/usr/bin/env python3
import json
import logging
import time
from functools import wraps
from json import JSONDecodeError
from mimetypes import add_type
from pathlib import Path
from typing import Callable, Optional

import httplib2
import httpx
import rich_click as click
import uvloop
from click.exceptions import BadParameter
from googleapiclient.discovery import Resource, build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from rich.logging import RichHandler

from .const import COOKIE_TXT, PATH
from .drive import upload_with_drive
from .scotty import steal_cookie, upload_with_scotty

logging.basicConfig(handlers=[RichHandler(rich_tracebacks=True)])

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
def main() -> None:
    pass


def verbose_flag(func):
    @click.option("--verbose", is_flag=True)
    @wraps(func)
    def wrapper(*args, **kwargs):
        verbose = kwargs.pop("verbose")
        logging.getLogger().setLevel(logging.DEBUG if verbose else logging.INFO)
        return func(*args, **kwargs)

    return wrapper


@main.command()
@click.argument(
    "files",
    required=True,
    nargs=-1,
    type=click.Path(exists=True, readable=True, path_type=Path, dir_okay=False),
)
@click.option("--use-drive", is_flag=True)
@click.option("--bookshelf")
@verbose_flag
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


def load_json(ctx, param, filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except JSONDecodeError as e:
        raise BadParameter(e) from e


@main.command()
@click.argument(
    "filename",
    type=click.Path(exists=True, readable=True, path_type=Path, dir_okay=False),
    callback=load_json,
)
@click.pass_context
@verbose_flag
def steal(ctx, data: dict):
    """
    Steal the cookie from a Chrome net-export log
    """
    cookie = steal_cookie(data)
    if not cookie:
        raise Exception("Could not find cookie")
    PATH.mkdir(parents=True, exist_ok=True)
    COOKIE_TXT.write_text(cookie)


@main.command()
@verbose_flag
def rpc():
    uvloop.run(_rpc())


async def _rpc():
    from ghunt.helpers import auth

    from .endpoints import LibraryService

    client = httpx.AsyncClient()

    creds = await auth.load_and_auth(client)

    service = LibraryService(creds, client)
    logging.info("tags: %s", await service.list_tags())


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
