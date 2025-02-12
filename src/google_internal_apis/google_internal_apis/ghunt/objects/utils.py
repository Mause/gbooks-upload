from typing import *

from rich.console import Console

from ..errors import *
from .utils import *


class TMPrinter:
    """
    Print temporary text, on the same line.
    """

    def __init__(self, rc: Console = Console(highlight=False)):
        self.max_len = 0
        self.rc = rc

    def out(self, text: str, style: str = ""):
        if len(text) > self.max_len:
            self.max_len = len(text)
        else:
            text += " " * (self.max_len - len(text))
        self.rc.print(text, end="\r", style=style)

    def clear(self):
        self.rc.print(" " * self.max_len, end="\r")
