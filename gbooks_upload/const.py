from pathlib import Path

from platformdirs import user_cache_dir

PATH = Path(user_cache_dir("gbooks-upload", "Elliana May"))
COOKIE_TXT = PATH / "cookie.txt"
