from importlib.metadata import version

from click_man.shell import cli

cli(["gbooks-upload", "--man-version", version("gbooks-upload")])
