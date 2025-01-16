from asyncio import get_event_loop

import httpx
from ghunt.helpers import auth
from ghunt.knowledge.keys import keys

from .ghunter import PlayBooksPaRpc

keys["play"] = {
    "key": "AIzaSyCWq1--9JnN9QM7k57Rc_qmt9c0OVy0rME",
    "origin": "https://play.google.com",
}


async def ghunt(service, method):
    client = httpx.AsyncClient()

    creds = await auth.load_and_auth(client)

    api = PlayBooksPaRpc(creds)

    return await api.call_rpc(method, client)


class RpcService:
    def __init__(self):
        assert getattr(self, "service", None)

    def call_rpc(self, method: str):
        return get_event_loop().run_until_complete(ghunt(self.service, method))


class EnterpriseService(RpcService):
    service = "enterprise.v1.EnterpriseService"

    def get_licenses(self):
        return self.call_rpc("GetLicenses")

    def list_free_books_for_license(self):
        return self.call_rpc("ListFreeBooksForLicense")


class SettingsOnePlatformService(RpcService):
    service = "settings.v1.SettingsOnePlatformService"

    def get_user_settings(self):
        return self.call_rpc("GetUserSettings")


class SeriesOnePlatformService(RpcService):
    service = "series.v1.SeriesOnePlatformService"

    def fetch(self):
        return self.call_rpc("Fetch")


class LibraryService(RpcService):
    service = "library.v1.LibraryService"

    def list_tags(self):
        return self.call_rpc("ListTags")

    def sync_user_library(self):
        return self.call_rpc("SyncUserLibrary")

    def sync_extended_library(self):
        return self.call_rpc("SyncExtendedLibrary")
