from .ghunter import RpcService


class InternalPeopleService(RpcService):
    hostname = "people-pa.clients6.google.com"
    service = "google.internal.people.v2.InternalPeopleService"

    async def get_people(
        self,
        data='[["me"],[[["person.name","person.email","person.photo"]],null,[5,1,7]]]',
    ):
        return await self.call_rpc("GetPeople", data=data)


class AudiobookService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.audiobook.v1.AudiobookService"

    async def get_audiobook_resource(self):
        return await self.call_rpc("GetAudiobookResource")

    async def get_audiobook_supplement(self):
        return await self.call_rpc("GetAudiobookSupplement")


class CloudLoadingOnePlatformService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = (
        "google.internal.play.books.cloudloading.v1.CloudLoadingOnePlatformService"
    )

    async def delete(self):
        return await self.call_rpc("Delete")

    async def insert(self):
        return await self.call_rpc("Insert")


class EnterpriseService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.enterprise.v1.EnterpriseService"

    async def add_classroom_books_attachment(self):
        return await self.call_rpc("AddClassroomBooksAttachment")

    async def add_license_owners(self):
        return await self.call_rpc("AddLicenseOwners")

    async def add_license_redeemers(self):
        return await self.call_rpc("AddLicenseRedeemers")

    async def claim_license(self):
        return await self.call_rpc("ClaimLicense")

    async def get_license_history(self):
        return await self.call_rpc("GetLicenseHistory")

    async def get_licenses(self, data="[null,null,null,1]"):
        return await self.call_rpc("GetLicenses", data=data)

    async def grant_free_book_licenses(self):
        return await self.call_rpc("GrantFreeBookLicenses")

    async def list_free_books_for_license(self):
        return await self.call_rpc("ListFreeBooksForLicense")

    async def remove_license_owners(self):
        return await self.call_rpc("RemoveLicenseOwners")

    async def remove_license_redeemers(self):
        return await self.call_rpc("RemoveLicenseRedeemers")


class FamilyOnePlatformService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.family.v1.FamilyOnePlatformService"

    async def share(self):
        return await self.call_rpc("Share")

    async def unshare(self):
        return await self.call_rpc("Unshare")


class VolumeAnnotationService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.layers.v1.VolumeAnnotationService"

    async def get_dictionary_definition(
        self, data='[null," unwrapping",[null,null,"en"]]'
    ):
        return await self.call_rpc("GetDictionaryDefinition", data=data)


class LibraryService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.library.v1.LibraryService"

    async def add_library_document(self):
        return await self.call_rpc("AddLibraryDocument")

    async def add_tags(self):
        return await self.call_rpc("AddTags")

    async def create_custom_tag(self):
        return await self.call_rpc("CreateCustomTag")

    async def delete_custom_tag(self):
        return await self.call_rpc("DeleteCustomTag")

    async def delete_library_document(self):
        return await self.call_rpc("DeleteLibraryDocument")

    async def expunge_library_documents(self):
        return await self.call_rpc("ExpungeLibraryDocuments")

    async def get_library_document(self):
        return await self.call_rpc("GetLibraryDocument")

    async def get_volume_overviews(self):
        return await self.call_rpc("GetVolumeOverviews")

    async def hide_library_documents(self):
        return await self.call_rpc("HideLibraryDocuments")

    async def list_tags(self):
        return await self.call_rpc("ListTags")

    async def lookup_copy_limit(self):
        return await self.call_rpc("LookupCopyLimit")

    async def remove_tags(self):
        return await self.call_rpc("RemoveTags")

    async def sync_document_position(
        self,
        data='["84XKNwAAAEAJ",["384DC38E-1A56-4F48-8AE1-1C3F446F41E5",null,"1737093647557",[null,null,[2]],null,[["GBS.PA68.w.0.0.0.2"],null,0.9066666666666666]]]',
    ):
        return await self.call_rpc("SyncDocumentPosition", data=data)

    async def sync_extended_library(self):
        return await self.call_rpc("SyncExtendedLibrary")

    async def sync_user_library(self):
        return await self.call_rpc("SyncUserLibrary")

    async def unhide_library_documents(self):
        return await self.call_rpc("UnhideLibraryDocuments")

    async def update_copy_limit(self):
        return await self.call_rpc("UpdateCopyLimit")

    async def update_custom_tag(self):
        return await self.call_rpc("UpdateCustomTag")


class SeriesOnePlatformService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.series.v1.SeriesOnePlatformService"

    async def fetch(
        self,
        data='[[["u4P3GgAAABBNmM"],["PL4pGwAAABAUpM"],["bW8uGwAAABBCdM"],["i1YuGwAAABCkTM"],["crbMGgAAABC_rM"]]]',
    ):
        return await self.call_rpc("Fetch", data=data)

    async def fetch_members(self):
        return await self.call_rpc("FetchMembers")


class SettingsOnePlatformService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.settings.v1.SettingsOnePlatformService"

    async def get_user_settings(self):
        return await self.call_rpc("GetUserSettings")

    async def update_user_settings(self):
        return await self.call_rpc("UpdateUserSettings")


class UserAnnotationService(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.userannotations.v1.UserAnnotationService"

    async def create_annotations(self):
        return await self.call_rpc("CreateAnnotations")

    async def create_collection(self):
        return await self.call_rpc("CreateCollection")

    async def delete_annotations(self):
        return await self.call_rpc("DeleteAnnotations")

    async def delete_collection(self):
        return await self.call_rpc("DeleteCollection")

    async def list_annotations(
        self, data='[[["84XKNwAAAEAJ",null,"full-1.0.0"]],[1,2],null,1,1]'
    ):
        return await self.call_rpc("ListAnnotations", data=data)

    async def list_shared_annotations(
        self, data='[["84XKNwAAAEAJ",null,"full-1.0.0"],1,null,null,1]'
    ):
        return await self.call_rpc("ListSharedAnnotations", data=data)

    async def trigger_export(self):
        return await self.call_rpc("TriggerExport")

    async def update_annotations(self):
        return await self.call_rpc("UpdateAnnotations")

    async def update_collection(self):
        return await self.call_rpc("UpdateCollection")

    async def update_subscriptions(self):
        return await self.call_rpc("UpdateSubscriptions")


class PlayGatewayBooksService(RpcService):
    hostname = "playgateway-pa.clients6.google.com"
    service = "play.gateway.adapter.books.v1.PlayGatewayBooksService"

    async def get_in_app_stream(
        self,
        data='[[4,null,["84XKNwAAAEAJ",1]],null,null,null,null,[null,null,null,null,null,null,[3]],null,null,[null,[2],[1]]]',
    ):
        return await self.call_rpc("GetInAppStream", data=data)


class Waa(RpcService):
    hostname = "waa-pa.clients6.google.com"
    service = "google.internal.waa.v1.Waa"

    async def ping(self):
        return await self.call_rpc("Ping")
