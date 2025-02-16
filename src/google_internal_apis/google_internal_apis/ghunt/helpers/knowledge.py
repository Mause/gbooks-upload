from ..errors import GHuntKnowledgeError
from ..knowledge.keys import keys
from ..knowledge.services import services_baseurls
from ..knowledge.sig import sigs


def get_domain_of_service(service: str) -> str:
    if service not in services_baseurls:
        raise GHuntKnowledgeError(
            f'The service "{service}" has not been found in GHunt\'s services knowledge.'
        )
    return services_baseurls.get(service)


def get_origin_of_key(key_name: str) -> str:
    if key_name not in keys:
        raise GHuntKnowledgeError(
            f'The key "{key_name}" has not been found in GHunt\'s API keys knowledge.'
        )
    return keys.get(key_name, {}).get("origin")


def get_api_key(key_name: str) -> str:
    if key_name not in keys:
        raise GHuntKnowledgeError(
            f'The key "{key_name}" has not been found in GHunt\'s API keys knowledge.'
        )
    return keys.get(key_name, {}).get("key")


def get_package_sig(package_name: str) -> str:
    if package_name not in sigs:
        raise GHuntKnowledgeError(
            f'The package name "{package_name}" has not been found in GHunt\'s SIGs knowledge.'
        )
    return sigs.get(package_name)
