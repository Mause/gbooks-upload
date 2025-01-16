import inspect
from email.message import Message

import ghunt.globals as gb
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds


def camel(s: str):
    return "".join(word.title() for word in s.split("_"))


class PeoplePaHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict[str, str] = {}):
        super().__init__()

        if not headers:
            headers = gb.config.headers

        base_headers = {
            "Content-Type": "application/json+protobuf",
            "X-User-Agent": "grpc-web-javascript/0.1",
        }

        headers = {**headers, **base_headers}

        self.hostname = "playbooks-pa.clients6.google.com"
        self.scheme = "https"
        self.service = "google.internal.play.books.library.v1.LibraryService"

        self.authentication_mode = (
            "sapisidhash"  # sapisidhash, cookies_only, oauth or None
        )
        self.require_key = "play"  # key name, or None

        self._load_api(creds, headers)

    async def list_tags(self, as_client: httpx.AsyncClient):
        method = camel(inspect.currentframe().f_code.co_name)

        self._load_endpoint(method)

        message = Message()
        for k, v in self.loaded_endpoints[method].headers.items():
            message.add_header(k, v)

        return (
            await self._query(
                as_client,
                "POST",
                method,
                f"/$rpc/{self.service}/{method}",
                {"$httpHeaders": message.as_string()},
                None,
                "json",
            )
        ).json()
