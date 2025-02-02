from datetime import datetime
from pprint import pformat

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import StringValue

from google_internal_apis import LibraryServiceRpc
from input_pb2 import TagsResponse


def repeated(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        for array in value:
            parse(array, getattr(message, field.name))
    else:
        getattr(message, field.name).extend(value)


def parse(arrays, message):
    fields = message.DESCRIPTOR.fields
    if isinstance(message, Timestamp):
        message.FromMilliseconds(int(arrays))
        return message
    if isinstance(message, StringValue):
        if arrays:
            message.MergeFromString(arrays)
        return message

    for field in fields:
        value = arrays[field.number - 1]
        if field.label == field.LABEL_REPEATED:
            repeated(message, field, value)
        elif field.label == field.LABEL_REQUIRED:
            if field.type == field.TYPE_MESSAGE:
                parse(value, getattr(message, field.name))
            else:
                setattr(message, field.name, value)
        elif field.label == field.LABEL_OPTIONAL:
            if field.type == field.TYPE_MESSAGE:
                parse(value, getattr(message, field.name))
            else:
                setattr(message, field.name, value)
        else:
            raise ValueError("Unknown label")
    remaining = arrays[fields[-1].number :]
    if remaining:
        raise ValueError("Extra fields: " + pformat(remaining))
    return message


class LibraryService(LibraryServiceRpc):
    async def add_tags(self, book_ids, tag_id):
        return await super().add_tags(
            [
                [
                    [book_id, tag_id, str(int(datetime.now().timestamp() * 1000))]
                    for book_id in book_ids
                ]
            ]
        )

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
