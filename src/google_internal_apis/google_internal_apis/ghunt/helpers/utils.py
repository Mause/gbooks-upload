import hashlib
import logging
from copy import deepcopy
from time import time
from typing import Dict

import httpx

logger = logging.getLogger(__name__)


def gen_sapisidhash(
    sapisid: str, origin: str, timestamp: str = str(int(time()))
) -> str:
    return f"{timestamp}_{hashlib.sha1(' '.join([timestamp, sapisid, origin]).encode()).hexdigest()}"


def inject_osid(
    cookies: Dict[str, str], osids: Dict[str, str], service: str
) -> Dict[str, str]:
    cookies_with_osid = deepcopy(cookies)
    cookies_with_osid["OSID"] = osids[service]
    return cookies_with_osid


def is_headers_syntax_good(headers: Dict[str, str]) -> bool:
    try:
        httpx.Headers(headers)
        return True
    except Exception:
        logger.error("Invalid headers syntax")
        return False


def parse_oauth_flow_response(body: str):
    """
    Correctly format the response sent by android.googleapis.com
    during the Android OAuth2 Login Flow.
    """
    return {sp[0]: "=".join(sp[1:]) for x in body.split("\n") if (sp := x.split("="))}
