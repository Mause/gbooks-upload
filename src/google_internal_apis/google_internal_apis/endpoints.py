from .ghunter import RpcService


class WhApiServiceRpc(RpcService):
    service = "google.internal.play.atoms.api.v1.WhApiService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playatoms-pa.clients6.google.com"

    async def get_app_splits(self, data=None):
        return await self._call_rpc("GetAppSplits", data=data)

    async def update_user_prefs(self, data=None):
        return await self._call_rpc("UpdateUserPrefs", data=data)

    async def get_domain_filter(self, data=None):
        return await self._call_rpc("GetDomainFilter", data=data)

    async def get_intent_filter(self, data=None):
        return await self._call_rpc("GetIntentFilter", data=data)


class AppointmentBookingServiceRpc(RpcService):
    service = "google.internal.calendar.v1.AppointmentBookingService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "calendar-pa.clients6.google.com"

    async def list_available_slots(self, data=None):
        return await self._call_rpc("ListAvailableSlots", data=data)


class PairingRpc(RpcService):
    service = "google.internal.communications.instantmessaging.v1.Pairing"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "instantmessaging-pa.googleapis.com"

    async def register_phone_relay(self, data=None):
        return await self._call_rpc("RegisterPhoneRelay", data=data)

    async def refresh_phone_relay(self, data=None):
        return await self._call_rpc("RefreshPhoneRelay", data=data)

    async def get_web_encryption_key(self, data=None):
        return await self._call_rpc("GetWebEncryptionKey", data=data)

    async def revoke_relay_pairing(self, data=None):
        return await self._call_rpc("RevokeRelayPairing", data=data)


class MessagingRpc(RpcService):
    service = "google.internal.communications.instantmessaging.v1.Messaging"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "instantmessaging-pa.googleapis.com"

    async def receive_messages(self, data=None):
        return await self._call_rpc("ReceiveMessages", data=data)

    async def send_message(self, data=None):
        return await self._call_rpc("SendMessage", data=data)

    async def ack_messages(self, data=None):
        return await self._call_rpc("AckMessages", data=data)


class RegistrationRpc(RpcService):
    service = "google.internal.communications.instantmessaging.v1.Registration"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "instantmessaging-pa.googleapis.com"

    async def sign_in_gaia(self, data=None):
        return await self._call_rpc("SignInGaia", data=data)

    async def register_refresh(self, data=None):
        return await self._call_rpc("RegisterRefresh", data=data)


class MeetingDeviceServiceRpc(RpcService):
    service = "google.rtc.meetings.v1.MeetingDeviceService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "meet.google.com"

    async def create_meeting_device(self, data=None):
        return await self._call_rpc("CreateMeetingDevice", data=data)


class MeetingSpaceServiceRpc(RpcService):
    service = "google.rtc.meetings.v1.MeetingSpaceService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "meet.google.com"

    async def sync_meeting_space_collections(self, data=None):
        return await self._call_rpc("SyncMeetingSpaceCollections", data=data)


class InternalPeopleServiceRpc(RpcService):
    service = "google.internal.people.v2.InternalPeopleService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "people-pa.clients6.google.com"

    async def get_people(
        self,
        data='[["me"],[[["person.name","person.email","person.photo"]],null,[5,1,7]]]',
    ):
        return await self._call_rpc("GetPeople", data=data)

    async def get_person_photo_encoded(self, data=None):
        return await self._call_rpc("GetPersonPhotoEncoded", data=data)

    async def update_person_photo(self, data=None):
        return await self._call_rpc("UpdatePersonPhoto", data=data)


class InternalPeopleMinimalServiceRpc(RpcService):
    service = "google.internal.people.v2.minimal.InternalPeopleMinimalService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "people-pa.clients6.google.com"

    async def list_ranked_targets(self, data=None):
        return await self._call_rpc("ListRankedTargets", data=data)

    async def list_people_by_known_id(self, data=None):
        return await self._call_rpc("ListPeopleByKnownId", data=data)


class AudiobookServiceRpc(RpcService):
    service = "google.internal.play.books.audiobook.v1.AudiobookService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def get_audio_events(
        self, data='["AQAAAEAszz6PAM","8af46ef0d127346baff59518",[8],4976830,6776830]'
    ):
        return await self._call_rpc("GetAudioEvents", data=data)

    async def get_audiobook_resource(self, data=None):
        return await self._call_rpc("GetAudiobookResource", data=data)

    async def get_audiobook_supplement(self, data=None):
        return await self._call_rpc("GetAudiobookSupplement", data=data)


class CloudLoadingOnePlatformServiceRpc(RpcService):
    service = (
        "google.internal.play.books.cloudloading.v1.CloudLoadingOnePlatformService"
    )

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def delete(self, data=None):
        return await self._call_rpc("Delete", data=data)

    async def insert(self, data=None):
        return await self._call_rpc("Insert", data=data)


class EnterpriseServiceRpc(RpcService):
    service = "google.internal.play.books.enterprise.v1.EnterpriseService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def add_classroom_books_attachment(self, data=None):
        return await self._call_rpc("AddClassroomBooksAttachment", data=data)

    async def add_license_owners(self, data=None):
        return await self._call_rpc("AddLicenseOwners", data=data)

    async def add_license_redeemers(self, data=None):
        return await self._call_rpc("AddLicenseRedeemers", data=data)

    async def claim_license(self, data=None):
        return await self._call_rpc("ClaimLicense", data=data)

    async def get_license_history(self, data=None):
        return await self._call_rpc("GetLicenseHistory", data=data)

    async def get_licenses(self, data="[null,null,null,1]"):
        return await self._call_rpc("GetLicenses", data=data)

    async def grant_free_book_licenses(self, data=None):
        return await self._call_rpc("GrantFreeBookLicenses", data=data)

    async def list_free_books_for_license(self, data=None):
        return await self._call_rpc("ListFreeBooksForLicense", data=data)

    async def remove_license_owners(self, data=None):
        return await self._call_rpc("RemoveLicenseOwners", data=data)

    async def remove_license_redeemers(self, data=None):
        return await self._call_rpc("RemoveLicenseRedeemers", data=data)


class FamilyOnePlatformServiceRpc(RpcService):
    service = "google.internal.play.books.family.v1.FamilyOnePlatformService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def share(self, data=None):
        return await self._call_rpc("Share", data=data)

    async def unshare(self, data=None):
        return await self._call_rpc("Unshare", data=data)


class VolumeAnnotationServiceRpc(RpcService):
    service = "google.internal.play.books.layers.v1.VolumeAnnotationService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def get_dictionary_definition(
        self, data='[null," unwrapping",[null,null,"en"]]'
    ):
        return await self._call_rpc("GetDictionaryDefinition", data=data)


class LibraryServiceRpc(RpcService):
    service = "google.internal.play.books.library.v1.LibraryService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def add_annotation(
        self,
        data='[["AQAAAEAszz6PAM","AE67D741-9B6D-4C7D-B170-312AF12BE063",[],null,null,[["40102"]],"0.10.0"]]',
    ):
        return await self._call_rpc("AddAnnotation", data=data)

    async def add_library_document(self, data=None):
        return await self._call_rpc("AddLibraryDocument", data=data)

    async def add_tags(
        self, data='[[["5QuwNwAAAEAJ","a0c746137-5723-4740-89a8-4ef7311aad16"]]]'
    ):
        return await self._call_rpc("AddTags", data=data)

    async def create_custom_tag(self, data=None):
        return await self._call_rpc("CreateCustomTag", data=data)

    async def delete_annotation(self, data=None):
        return await self._call_rpc("DeleteAnnotation", data=data)

    async def delete_custom_tag(self, data=None):
        return await self._call_rpc("DeleteCustomTag", data=data)

    async def delete_library_document(self, data=None):
        return await self._call_rpc("DeleteLibraryDocument", data=data)

    async def expunge_library_documents(self, data=None):
        return await self._call_rpc("ExpungeLibraryDocuments", data=data)

    async def get_library_document(self, data='[[], "hdYTCAAAQBAJ"]'):
        return await self._call_rpc("GetLibraryDocument", data=data)

    async def get_volume_overviews(self, data=None):
        return await self._call_rpc("GetVolumeOverviews", data=data)

    async def hide_library_documents(self, data=None):
        return await self._call_rpc("HideLibraryDocuments", data=data)

    async def list_annotations(self, data=None):
        return await self._call_rpc("ListAnnotations", data=data)

    async def list_tags(self, data=None):
        return await self._call_rpc("ListTags", data=data)

    async def lookup_copy_limit(self, data=None):
        return await self._call_rpc("LookupCopyLimit", data=data)

    async def remove_tags(self, data='[[["hdYTCAAAQBAJ","Completed",1737103382078]]]'):
        return await self._call_rpc("RemoveTags", data=data)

    async def sync_document_position(
        self,
        data='["84XKNwAAAEAJ",["384DC38E-1A56-4F48-8AE1-1C3F446F41E5",null,"1737093647557",[null,null,[2]],null,[["GBS.PA68.w.0.0.0.2"],null,0.9066666666666666]]]',
    ):
        return await self._call_rpc("SyncDocumentPosition", data=data)

    async def sync_extended_library(self, data=None):
        return await self._call_rpc("SyncExtendedLibrary", data=data)

    async def sync_user_library(self, data=None):
        return await self._call_rpc("SyncUserLibrary", data=data)

    async def unhide_library_documents(self, data=None):
        return await self._call_rpc("UnhideLibraryDocuments", data=data)

    async def update_copy_limit(self, data=None):
        return await self._call_rpc("UpdateCopyLimit", data=data)

    async def update_custom_tag(
        self, data='["a0c746137-5723-4740-89a8-4ef7311aad16","test 1"]'
    ):
        return await self._call_rpc("UpdateCustomTag", data=data)


class SeriesOnePlatformServiceRpc(RpcService):
    service = "google.internal.play.books.series.v1.SeriesOnePlatformService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def fetch(
        self,
        data='[[["u4P3GgAAABBNmM"],["PL4pGwAAABAUpM"],["bW8uGwAAABBCdM"],["i1YuGwAAABCkTM"],["crbMGgAAABC_rM"]]]',
    ):
        return await self._call_rpc("Fetch", data=data)

    async def fetch_members(self, data='[["u4P3GgAAABBNmM"],[100]]'):
        return await self._call_rpc("FetchMembers", data=data)


class SettingsOnePlatformServiceRpc(RpcService):
    service = "google.internal.play.books.settings.v1.SettingsOnePlatformService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def get_user_settings(self, data=None):
        return await self._call_rpc("GetUserSettings", data=data)

    async def update_user_settings(self, data=None):
        return await self._call_rpc("UpdateUserSettings", data=data)


class UserAnnotationServiceRpc(RpcService):
    service = "google.internal.play.books.userannotations.v1.UserAnnotationService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playbooks-pa.clients6.google.com"

    async def create_annotations(self, data=None):
        return await self._call_rpc("CreateAnnotations", data=data)

    async def create_collection(self, data=None):
        return await self._call_rpc("CreateCollection", data=data)

    async def delete_annotations(self, data=None):
        return await self._call_rpc("DeleteAnnotations", data=data)

    async def delete_collection(self, data=None):
        return await self._call_rpc("DeleteCollection", data=data)

    async def list_annotations(
        self, data='[[["84XKNwAAAEAJ",null,"full-1.0.0"]],[1,2],null,1,1]'
    ):
        return await self._call_rpc("ListAnnotations", data=data)

    async def list_shared_annotations(
        self, data='[["84XKNwAAAEAJ",null,"full-1.0.0"],1,null,null,1]'
    ):
        return await self._call_rpc("ListSharedAnnotations", data=data)

    async def trigger_export(self, data=None):
        return await self._call_rpc("TriggerExport", data=data)

    async def update_annotations(self, data=None):
        return await self._call_rpc("UpdateAnnotations", data=data)

    async def update_collection(self, data=None):
        return await self._call_rpc("UpdateCollection", data=data)

    async def update_subscriptions(self, data=None):
        return await self._call_rpc("UpdateSubscriptions", data=data)


class PlayGatewayBooksServiceRpc(RpcService):
    service = "play.gateway.adapter.books.v1.PlayGatewayBooksService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "playgateway-pa.clients6.google.com"

    async def get_in_app_stream(
        self,
        data='[[4,null,["84XKNwAAAEAJ",1]],null,null,null,null,[null,null,null,null,null,null,[3]],null,null,[null,[2],[1]]]',
    ):
        return await self._call_rpc("GetInAppStream", data=data)

    async def update_item_wishlist_state(self, data='[null,[\\"ID07FerN_h0C\\",9],1]'):
        return await self._call_rpc("UpdateItemWishlistState", data=data)


class MakerSuiteServiceRpc(RpcService):
    service = "google.internal.alkali.applications.makersuite.v1.MakerSuiteService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "alkalimakersuite-pa.clients6.google.com"

    async def generate_content(self, data=None):
        return await self._call_rpc("GenerateContent", data=data)

    async def create_tuned_model(self, data=None):
        return await self._call_rpc("CreateTunedModel", data=data)


class MetricServiceRpc(RpcService):
    service = "google.internal.alkali.applications.metricsink.v1.MetricService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "alkalimetricsink-pa.clients6.google.com"

    async def record_metrics(self, data=None):
        return await self._call_rpc("RecordMetrics", data=data)


class ProfileServiceRpc(RpcService):
    service = "google.internal.developerprofiles.v1.profile.ProfileService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "developerprofiles-pa.clients6.google.com"

    async def get_public_profile(self, data=None):
        return await self._call_rpc("GetPublicProfile", data=data)


class MapsJsInternalServiceRpc(RpcService):
    service = "google.internal.maps.mapsjs.v1.MapsJsInternalService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "maps.googleapis.com"

    async def get_metadata(self, data=None):
        return await self._call_rpc("GetMetadata", data=data)

    async def single_image_search(self, data=None):
        return await self._call_rpc("SingleImageSearch", data=data)


class AddOnServiceRpc(RpcService):
    service = "google.internal.apps.addons.v1.AddOnService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "addons-pa.clients6.google.com"

    async def list_installations(self, data=None):
        return await self._call_rpc("ListInstallations", data=data)


class SpeechRpc(RpcService):
    service = "google.cloud.speech.v1.Speech"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "speech.googleapis.com"

    async def recognize(self, data=None):
        return await self._call_rpc("Recognize", data=data)


class MetadataServiceRpc(RpcService):
    service = "fonts.fe.catalog.actions.metadata.MetadataService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "fonts.google.com"

    async def sample_text(self, data=None):
        return await self._call_rpc("SampleText", data=data)

    async def family_detail(self, data=None):
        return await self._call_rpc("FamilyDetail", data=data)

    async def license(self, data=None):
        return await self._call_rpc("License", data=data)


class PeopleStackExperimentsServiceRpc(RpcService):
    service = "peoplestackwebexperiments.PeopleStackExperimentsService"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "peoplestackwebexperiments-pa.clients6.google.com"

    async def get_experiment_flags(self, data=None):
        return await self._call_rpc("GetExperimentFlags", data=data)


class WaaRpc(RpcService):
    service = "google.internal.waa.v1.Waa"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "waa-pa.clients6.google.com"

    async def create(self, data=None):
        return await self._call_rpc("Create", data=data)

    async def ping(self, data=None):
        return await self._call_rpc("Ping", data=data)
