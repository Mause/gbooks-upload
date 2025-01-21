from datetime import datetime

from .endpoints_rpc import LibraryServiceRpc


class LibraryService:
    def __init__(self, creds, client):
        self._library = LibraryServiceRpc(creds, client)

    async def list_tags(self):
        [tags, tagged] = await self._library.list_tags()

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
