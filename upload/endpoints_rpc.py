from .ghunter import RpcService


class InternalPeopleServiceRpc(RpcService):
    hostname = "people-pa.clients6.google.com"
    service = "google.internal.people.v2.InternalPeopleService"

    async def get_people(
        self,
        data='[["me"],[[["person.name","person.email","person.photo"]],null,[5,1,7]]]',
    ):
        return await self._call_rpc("GetPeople", data=data)

    async def get_person_photo_encoded(self):
        return await self._call_rpc("GetPersonPhotoEncoded")

    async def update_person_photo(self):
        return await self._call_rpc("UpdatePersonPhoto")


class AudiobookServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.audiobook.v1.AudiobookService"

    async def get_audio_events(
        self, data='["AQAAAEAszz6PAM","8af46ef0d127346baff59518",[8],4976830,6776830]'
    ):
        return await self._call_rpc("GetAudioEvents", data=data)

    async def get_audiobook_resource(self):
        return await self._call_rpc("GetAudiobookResource")

    async def get_audiobook_supplement(self):
        return await self._call_rpc("GetAudiobookSupplement")


class CloudLoadingOnePlatformServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = (
        "google.internal.play.books.cloudloading.v1.CloudLoadingOnePlatformService"
    )

    async def delete(self):
        return await self._call_rpc("Delete")

    async def insert(self):
        return await self._call_rpc("Insert")


class EnterpriseServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.enterprise.v1.EnterpriseService"

    async def add_classroom_books_attachment(self):
        return await self._call_rpc("AddClassroomBooksAttachment")

    async def add_license_owners(self):
        return await self._call_rpc("AddLicenseOwners")

    async def add_license_redeemers(self):
        return await self._call_rpc("AddLicenseRedeemers")

    async def claim_license(self):
        return await self._call_rpc("ClaimLicense")

    async def get_license_history(self):
        return await self._call_rpc("GetLicenseHistory")

    async def get_licenses(self, data="[null,null,null,1]"):
        return await self._call_rpc("GetLicenses", data=data)

    async def grant_free_book_licenses(self):
        return await self._call_rpc("GrantFreeBookLicenses")

    async def list_free_books_for_license(self):
        return await self._call_rpc("ListFreeBooksForLicense")

    async def remove_license_owners(self):
        return await self._call_rpc("RemoveLicenseOwners")

    async def remove_license_redeemers(self):
        return await self._call_rpc("RemoveLicenseRedeemers")


class FamilyOnePlatformServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.family.v1.FamilyOnePlatformService"

    async def share(self):
        return await self._call_rpc("Share")

    async def unshare(self):
        return await self._call_rpc("Unshare")


class VolumeAnnotationServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.layers.v1.VolumeAnnotationService"

    async def get_dictionary_definition(
        self, data='[null," unwrapping",[null,null,"en"]]'
    ):
        return await self._call_rpc("GetDictionaryDefinition", data=data)


class LibraryServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.library.v1.LibraryService"

    async def add_annotation(
        self,
        data='[["AQAAAEAszz6PAM","AE67D741-9B6D-4C7D-B170-312AF12BE063",[],null,null,[["40102"]],"0.10.0"]]',
    ):
        return await self._call_rpc("AddAnnotation", data=data)

    async def add_library_document(self):
        return await self._call_rpc("AddLibraryDocument")

    async def add_tags(
        self, data='[[["5QuwNwAAAEAJ","a0c746137-5723-4740-89a8-4ef7311aad16"]]]'
    ):
        return await self._call_rpc("AddTags", data=data)

    async def create_custom_tag(self):
        return await self._call_rpc("CreateCustomTag")

    async def delete_annotation(self):
        return await self._call_rpc("DeleteAnnotation")

    async def delete_custom_tag(self):
        return await self._call_rpc("DeleteCustomTag")

    async def delete_library_document(self):
        return await self._call_rpc("DeleteLibraryDocument")

    async def expunge_library_documents(self):
        return await self._call_rpc("ExpungeLibraryDocuments")

    async def get_library_document(self, data='[[], "hdYTCAAAQBAJ"]'):
        return await self._call_rpc("GetLibraryDocument", data=data)

    async def get_volume_overviews(self):
        return await self._call_rpc("GetVolumeOverviews")

    async def hide_library_documents(self):
        return await self._call_rpc("HideLibraryDocuments")

    async def list_annotations(self):
        return await self._call_rpc("ListAnnotations")

    async def list_tags(self):
        return await self._call_rpc("ListTags")

    async def lookup_copy_limit(self):
        return await self._call_rpc("LookupCopyLimit")

    async def remove_tags(self, data='[[["hdYTCAAAQBAJ","Completed",1737103382078]]]'):
        return await self._call_rpc("RemoveTags", data=data)

    async def sync_document_position(
        self,
        data='["84XKNwAAAEAJ",["384DC38E-1A56-4F48-8AE1-1C3F446F41E5",null,"1737093647557",[null,null,[2]],null,[["GBS.PA68.w.0.0.0.2"],null,0.9066666666666666]]]',
    ):
        return await self._call_rpc("SyncDocumentPosition", data=data)

    async def sync_extended_library(self):
        return await self._call_rpc("SyncExtendedLibrary")

    async def sync_user_library(self):
        return await self._call_rpc("SyncUserLibrary")

    async def unhide_library_documents(self):
        return await self._call_rpc("UnhideLibraryDocuments")

    async def update_copy_limit(self):
        return await self._call_rpc("UpdateCopyLimit")

    async def update_custom_tag(
        self, data='["a0c746137-5723-4740-89a8-4ef7311aad16","test 1"]'
    ):
        return await self._call_rpc("UpdateCustomTag", data=data)


class SeriesOnePlatformServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.series.v1.SeriesOnePlatformService"

    async def fetch(
        self,
        data='[[["u4P3GgAAABBNmM"],["PL4pGwAAABAUpM"],["bW8uGwAAABBCdM"],["i1YuGwAAABCkTM"],["crbMGgAAABC_rM"]]]',
    ):
        return await self._call_rpc("Fetch", data=data)

    async def fetch_members(self, data='[["u4P3GgAAABBNmM"],[100]]'):
        return await self._call_rpc("FetchMembers", data=data)


class SettingsOnePlatformServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.settings.v1.SettingsOnePlatformService"

    async def get_user_settings(self):
        return await self._call_rpc("GetUserSettings")

    async def update_user_settings(self):
        return await self._call_rpc("UpdateUserSettings")


class UserAnnotationServiceRpc(RpcService):
    hostname = "playbooks-pa.clients6.google.com"
    service = "google.internal.play.books.userannotations.v1.UserAnnotationService"

    async def create_annotations(self):
        return await self._call_rpc("CreateAnnotations")

    async def create_collection(self):
        return await self._call_rpc("CreateCollection")

    async def delete_annotations(self):
        return await self._call_rpc("DeleteAnnotations")

    async def delete_collection(self):
        return await self._call_rpc("DeleteCollection")

    async def list_annotations(
        self, data='[[["84XKNwAAAEAJ",null,"full-1.0.0"]],[1,2],null,1,1]'
    ):
        return await self._call_rpc("ListAnnotations", data=data)

    async def list_shared_annotations(
        self, data='[["84XKNwAAAEAJ",null,"full-1.0.0"],1,null,null,1]'
    ):
        return await self._call_rpc("ListSharedAnnotations", data=data)

    async def trigger_export(self):
        return await self._call_rpc("TriggerExport")

    async def update_annotations(self):
        return await self._call_rpc("UpdateAnnotations")

    async def update_collection(self):
        return await self._call_rpc("UpdateCollection")

    async def update_subscriptions(self):
        return await self._call_rpc("UpdateSubscriptions")


class PlayGatewayBooksServiceRpc(RpcService):
    hostname = "playgateway-pa.clients6.google.com"
    service = "play.gateway.adapter.books.v1.PlayGatewayBooksService"

    async def get_in_app_stream(
        self,
        data='[[4,null,["84XKNwAAAEAJ",1]],null,null,null,null,[null,null,null,null,null,null,[3]],null,null,[null,[2],[1]]]',
    ):
        return await self._call_rpc("GetInAppStream", data=data)

    async def update_item_wishlist_state(self, data='[null,[\\"ID07FerN_h0C\\",9],1]'):
        return await self._call_rpc("UpdateItemWishlistState", data=data)


class WaaRpc(RpcService):
    hostname = "waa-pa.clients6.google.com"
    service = "google.internal.waa.v1.Waa"

    async def create(self):
        return await self._call_rpc("Create")

    async def ping(self):
        return await self._call_rpc("Ping")
