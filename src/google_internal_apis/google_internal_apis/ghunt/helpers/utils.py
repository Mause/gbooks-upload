from pathlib import Path

# from PIL import Image
import hashlib
from typing import *
from time import time
from datetime import datetime, timezone
from dateutil.parser import isoparse
from copy import deepcopy
import jsonpickle
import json
from packaging.version import parse as parse_version

import httpx

# import imagehash
from io import BytesIO

# from ghunt import globals as gb
from .. import version as current_version


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
    except:
        return False

