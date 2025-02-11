from datetime import datetime
from uuid import uuid4

from google_internal_apis import LibraryServiceRpc
from google_internal_apis.input_pb2 import (
    LibraryDocumentResponse,
    TagRequest,
    TagsResponse,
)
from google_internal_apis.json_format import dump, from_datetime, parse


class LibraryService(LibraryServiceRpc):
    async def add_tags(self, book_ids, tag_id):
        message = TagRequest(
            tagged_items=[
                {
                    "book_id": book_id,
                    "tag_id": tag_id,
                    "tagged_at": from_datetime(datetime.now()),
                }
                for book_id in book_ids
            ]
        )
        return await super().add_tags(dump(message))

    async def list_tags(self):
        res = parse(await super().list_tags(), TagsResponse())

        return {
            "tags": {tag.name: tag.tag_id for tag in res.tags},
            "tagged": [
                {
                    "book_id": tagged.book_id,
                    "tag_id": tagged.tag_id,
                    "tagged_at": tagged.tagged_at.ToDatetime(),
                }
                for tagged in res.tagged_items
            ],
        }

    async def get_library_document(self, book_id):
        return parse(
            await super().get_library_document([[], book_id]), LibraryDocumentResponse()
        )

    async def create_custom_tag(self, tag_name):
        ident = str(uuid4())
        await super().create_custom_tag([ident, tag_name])
        return ident
