from mimetypes import guess_type
from os.path import basename, splitext

from googleapiclient.discovery import Resource


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
