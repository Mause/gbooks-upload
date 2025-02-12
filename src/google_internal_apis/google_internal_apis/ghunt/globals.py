# This file is only intended to serve global variables at a project-wide level.


def init_globals():
    from rich.console import Console

    from .objects.utils import TMPrinter

    global config, tmprinter, rc

    from . import config

    tmprinter = TMPrinter()
    rc = Console(highlight=False)  # Rich Console
