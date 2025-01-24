from datetime import datetime

from google_internal_apis import LibraryServiceRpc


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
        [tags, tagged] = await super().list_tags()

        return {
            "tags": {name: tag_id for name, tag_id, *_ in tags},
            "tagged": [
                {
                    "book_id": book_id,
                    "tag_id": tag_id,
                    "tagged_at": datetime.fromtimestamp(int(tagged_at) / 1000),
                }
                for book_id, tag_id, tagged_at, *_ in tagged
            ],
        }
