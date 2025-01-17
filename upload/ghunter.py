from email.message import Message

import ghunt.globals as gb
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds


class PlayBooksPaRpc(GAPI):
    def __init__(self, service, creds: GHuntCreds, headers: dict[str, str] = {}):
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
        self.service = service

        self.authentication_mode = (
            "sapisidhash"  # sapisidhash, cookies_only, oauth or None
        )
        self.require_key = "play"  # key name, or None

        self._load_api(creds, headers)

    async def call_rpc(self, method, as_client: httpx.AsyncClient):
        self._load_endpoint(method)

        message = Message()
        for k, v in self.loaded_endpoints[method].headers.items():
            message.add_header(k, v)

        res = await self._query(
            as_client,
            "POST",
            method,
            f"/$rpc/{self.service}/{method}",
            {"$httpHeaders": message.as_string()},
            None,
            "json",
        )
        res.raise_for_status()
        return res.json()
