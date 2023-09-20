#!/usr/bin/env python3

import sys
import json
import time
import types
import logging
import argparse
from pprint import pprint
from os.path import splitext, basename, exists
from mimetypes import guess_type, add_type

import httplib2
import requests
from oauth2client.file import Storage
from oauth2client.tools import run_flow, argparser
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.discovery import build_from_document, build, Resource

logging.basicConfig(level=logging.DEBUG)
add_type('application/epub+zip', '.epub')

for service in ['books_v1', 'drive_v3']:
    filename = service + '.json'
    if not exists(filename):
        url = 'https://www.googleapis.com/discovery/v1/apis/{}/{}/rest'.format(
            *service.split('_')
        )
        with open(filename, 'wb') as fh:
            fh.write(requests.get(url).content)


def get_http():
    args = argparser.parse_args(["--noauth_local_webserver"])
    flow = flow_from_clientsecrets(
        'client_secrets.json',
        scope=[
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/books',
        ],
    )
    storage = Storage('credentials.json')
    credentials = storage.get()
    if credentials is None:
        credentials = run_flow(flags=args, flow=flow, storage=storage)
    http = credentials.authorize(httplib2.Http())
    if credentials.access_token_expired:
        credentials.refresh(http)
    return http


def upload(drive, books, filename):
    name = splitext(basename(filename))[0]
    mime_type = guess_type(filename)[0]

    response = (
        drive.files().create(media_body=filename, media_mime_type=mime_type).execute()
    )

    return (
        books.cloudloading()
        .addBook(
            # A drive document id. The upload_client_token must not be set.
            drive_document_id=response['id'],
            # The document MIME type.
            # It can be set only if the drive_document_id is set.
            mime_type=mime_type,
            # The document name.
            # It can be set only if the drive_document_id is set.
            name=name,
        )
        .execute()
    )


def get_volume(books: Resource, name: str = None, volumeId: str = None):
    return next(
        volume
        for volume in books.volumes().useruploaded().list().execute()['items']
        if (volume['volumeInfo']['title'] == name or volume['id'] == volumeId)
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    http = get_http()
    build = lambda filename: build_from_document(open(filename).read(), http=http)
    books = build('books_v1.json')
    drive = build('drive_v3.json')

    for filename in args.files:
        response = upload(drive, books, filename)

        monitor(books, response['volumeId'])


def monitor(books: Resource, volume_id: str) -> None:
    wait = 1

    while True:
        state = get_volume(books, volumeId=volume_id)['userInfo'][
            'userUploadedVolumeInfo'
        ]['processingState']
        print(state)
        if state.startswith('COMPLETED_'):
            break
        time.sleep(wait)
        wait *= 1.5


if __name__ == '__main__':
    main()
