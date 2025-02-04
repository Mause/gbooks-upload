Google Internal APIs
====================

Google has a lot of cool public APIs! But a lot of functionality is locked behind private, undocumented APIs.
This is a project to try to make them easier to consume, as many of them use a weird version of [Protobuf JSON](google_internal_apis/json_format.py) and [GRPC Protocol](google_internal_apis/ghunter.py).

```py
import asyncio
from google_internal_apis import get_client, LibraryService


async def main():
    client = await get_client(LibraryService)  # Google Play Books Library

    await client.get_tags()


if __name__ == '__main__':
    asyncio.run(main())
```
