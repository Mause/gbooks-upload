from email.message import Message

import ghunt.globals as gb
import httpx
from ghunt.knowledge.keys import keys
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds

keys.update(
    {
        "play": {
            "key": "AIzaSyCWq1--9JnN9QM7k57Rc_qmt9c0OVy0rME",
            "origin": "https://play.google.com",
        },
        "waa": {
            "key": "AIzaSyBGb5fGAyC-pRcRU6MUHb__b_vKha71HRE",
            "origin": "https://www.googleapis.com",  # TODO: confirm this value
        },
    }
)


class RpcService(GAPI):
    def __init__(
        self,
        creds: GHuntCreds,
        as_client: httpx.AsyncClient,
        headers: dict[str, str] = {},
    ):
        super().__init__()

        if not headers:
            headers = gb.config.headers

        base_headers = {
            "Content-Type": "application/json+protobuf",
            "X-User-Agent": "grpc-web-javascript/0.1",
        }

        headers = {**headers, **base_headers}

        self.scheme = "https"
        self.as_client = as_client

        self.authentication_mode = (
            "sapisidhash"  # sapisidhash, cookies_only, oauth or None
        )
        self.require_key = "play"  # key name, or None

        self._load_api(creds, headers)

    async def _call_rpc(self, method, data=None):
        self._load_endpoint(method)

        message = Message()
        for k, v in self.loaded_endpoints[method].headers.items():
            message.add_header(k, v)

        res = await self._query(
            self.as_client,
            "POST",
            method,
            f"/$rpc/{self.service}/{method}",
            {"$httpHeaders": message.as_string()},
            data,
            "data" if isinstance(data, str) else "json",
        )
        try:
            data = res.json()
        except ValueError:
            data = res.text
        if not res.is_success:
            raise Exception(res, data)
        return data
