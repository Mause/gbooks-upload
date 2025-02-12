from email.message import Message

from .ghunt import globals as gb
import httpx
from .ghunt.knowledge.keys import keys
from .ghunt.objects.apis import GAPI, EndpointConfig
from .ghunt.objects.base import GHuntCreds
gb.init_globals()

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

        self._load_api(creds, headers)

    async def _call_rpc(self, method, data=None):
        self._load_endpoint(
            EndpointConfig(
                name=method,
                verb="POST",
                headers=self.headers,
                data_type="data" if isinstance(data, str) else "json",
                authentication_mode="sapisidhash",
                require_key="play",
            )
        )

        message = Message()
        for k, v in self.loaded_endpoints[method]._computed_headers.items():
            message.add_header(k, v)

        res = await self._query(
            method,
            self.as_client,
            f"/$rpc/{self.service}/{method}",
            {"$httpHeaders": message.as_string()},
            data,
        )
        try:
            data = res.json()
        except ValueError:
            data = res.text
        if not res.is_success:
            raise Exception(res, data)
        return data
