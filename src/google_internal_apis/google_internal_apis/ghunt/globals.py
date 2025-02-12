# This file is only intended to serve global variables at a project-wide level.


def init_globals():
    from .objects.utils import TMPrinter
    from rich.console import Console

    global config, tmprinter, rc
    
    from .import config
    tmprinter = TMPrinter()
    rc = Console(highlight=False) # Rich Console
