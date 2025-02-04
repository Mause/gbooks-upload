from typing import TypeVar

import httpx
from ghunt.helpers import auth

from .endpoints import *  # noqa
from .ghunter import RpcService

__version__ = "0.3.0"
T = TypeVar("T", bound="RpcService")


async def get_client(t: type[T]) -> T:
    client = httpx.AsyncClient()
    creds = await auth.load_and_auth(client)
    return t(creds, client)
