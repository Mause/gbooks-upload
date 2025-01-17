from .ghunter import RpcService


class InternalPeopleService(RpcService):
    service = "google.internal.people.v2.InternalPeopleService"

    async def get_people(self):
        return await self.call_rpc("GetPeople")


class AudiobookService(RpcService):
    service = "google.internal.play.books.audiobook.v1.AudiobookService"

    async def get_audiobook_resource(self):
        return await self.call_rpc("GetAudiobookResource")

    async def get_audiobook_supplement(self):
        return await self.call_rpc("GetAudiobookSupplement")


class CloudLoadingOnePlatformService(RpcService):
    service = (
        "google.internal.play.books.cloudloading.v1.CloudLoadingOnePlatformService"
    )

    async def delete(self):
        return await self.call_rpc("Delete")

    async def insert(self):
        return await self.call_rpc("Insert")


class EnterpriseService(RpcService):
    service = "google.internal.play.books.enterprise.v1.EnterpriseService"

    async def add_classroom_books_attachment(self):
        return await self.call_rpc("AddClassroomBooksAttachment")

    async def get_licenses(self):
        return await self.call_rpc("GetLicenses")

    async def add_license_redeemers(self):
        return await self.call_rpc("AddLicenseRedeemers")

    async def list_free_books_for_license(self):
        return await self.call_rpc("ListFreeBooksForLicense")

    async def remove_license_redeemers(self):
        return await self.call_rpc("RemoveLicenseRedeemers")

    async def grant_free_book_licenses(self):
        return await self.call_rpc("GrantFreeBookLicenses")

    async def claim_license(self):
        return await self.call_rpc("ClaimLicense")

    async def add_license_owners(self):
        return await self.call_rpc("AddLicenseOwners")

    async def get_license_history(self):
        return await self.call_rpc("GetLicenseHistory")

    async def remove_license_owners(self):
        return await self.call_rpc("RemoveLicenseOwners")


class FamilyOnePlatformService(RpcService):
    service = "google.internal.play.books.family.v1.FamilyOnePlatformService"

    async def unshare(self):
        return await self.call_rpc("Unshare")

    async def share(self):
        return await self.call_rpc("Share")


class VolumeAnnotationService(RpcService):
    service = "google.internal.play.books.layers.v1.VolumeAnnotationService"

    async def get_dictionary_definition(self):
        return await self.call_rpc("GetDictionaryDefinition")


class LibraryService(RpcService):
    service = "google.internal.play.books.library.v1.LibraryService"

    async def delete_custom_tag(self):
        return await self.call_rpc("DeleteCustomTag")

    async def create_custom_tag(self):
        return await self.call_rpc("CreateCustomTag")

    async def remove_tags(self):
        return await self.call_rpc("RemoveTags")

    async def sync_extended_library(self):
        return await self.call_rpc("SyncExtendedLibrary")

    async def delete_library_document(self):
        return await self.call_rpc("DeleteLibraryDocument")

    async def get_library_document(self):
        return await self.call_rpc("GetLibraryDocument")

    async def update_copy_limit(self):
        return await self.call_rpc("UpdateCopyLimit")

    async def hide_library_documents(self):
        return await self.call_rpc("HideLibraryDocuments")

    async def update_custom_tag(self):
        return await self.call_rpc("UpdateCustomTag")

    async def unhide_library_documents(self):
        return await self.call_rpc("UnhideLibraryDocuments")

    async def lookup_copy_limit(self):
        return await self.call_rpc("LookupCopyLimit")

    async def get_volume_overviews(self):
        return await self.call_rpc("GetVolumeOverviews")

    async def sync_document_position(self):
        return await self.call_rpc("SyncDocumentPosition")

    async def add_tags(self):
        return await self.call_rpc("AddTags")

    async def add_library_document(self):
        return await self.call_rpc("AddLibraryDocument")

    async def list_tags(self):
        return await self.call_rpc("ListTags")

    async def sync_user_library(self):
        return await self.call_rpc("SyncUserLibrary")

    async def expunge_library_documents(self):
        return await self.call_rpc("ExpungeLibraryDocuments")


class SeriesOnePlatformService(RpcService):
    service = "google.internal.play.books.series.v1.SeriesOnePlatformService"

    async def fetch(self):
        return await self.call_rpc("Fetch")

    async def fetch_members(self):
        return await self.call_rpc("FetchMembers")


class SettingsOnePlatformService(RpcService):
    service = "google.internal.play.books.settings.v1.SettingsOnePlatformService"

    async def update_user_settings(self):
        return await self.call_rpc("UpdateUserSettings")

    async def get_user_settings(self):
        return await self.call_rpc("GetUserSettings")


class UserAnnotationService(RpcService):
    service = "google.internal.play.books.userannotations.v1.UserAnnotationService"

    async def update_subscriptions(self):
        return await self.call_rpc("UpdateSubscriptions")

    async def trigger_export(self):
        return await self.call_rpc("TriggerExport")

    async def list_annotations(self):
        return await self.call_rpc("ListAnnotations")

    async def update_annotations(self):
        return await self.call_rpc("UpdateAnnotations")

    async def update_collection(self):
        return await self.call_rpc("UpdateCollection")

    async def delete_annotations(self):
        return await self.call_rpc("DeleteAnnotations")

    async def create_collection(self):
        return await self.call_rpc("CreateCollection")

    async def list_shared_annotations(self):
        return await self.call_rpc("ListSharedAnnotations")

    async def create_annotations(self):
        return await self.call_rpc("CreateAnnotations")

    async def delete_collection(self):
        return await self.call_rpc("DeleteCollection")


class Waa(RpcService):
    service = "google.internal.waa.v1.Waa"

    async def ping(self):
        return await self.call_rpc("Ping")
