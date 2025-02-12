import json
from datetime import datetime


class GHuntEncoder(json.JSONEncoder):
    """
    Converts non-default types when exporting to JSON.
    """

    def default(self, o: object) -> dict:
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime):
            return f"{o.strftime('%Y/%m/%d %H:%M:%S')} (UTC)"
        if type(o) not in [str, list, int, float, bool, dict]:
            if hasattr(o, "__dict__"):
                return o.__dict__
            return {x: getattr(o, x) for x in o.__slots__}
