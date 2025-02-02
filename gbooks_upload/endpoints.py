from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp

from google_internal_apis import LibraryServiceRpc
from google_internal_apis.json_format import dump, parse
from input_pb2 import TagRequest, TagsResponse


class LibraryService(LibraryServiceRpc):
    async def add_tags(self, book_ids, tag_id):
        message = TagRequest()
        tagged_at = Timestamp()
        tagged_at.FromDatetime(datetime.now())
        for book_id in book_ids:
            message.tagged_items.add(
                book_id=book_id,
                tag_id=tag_id,
                tagged_at=tagged_at,
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
        return await super().get_library_document([[], book_id])
