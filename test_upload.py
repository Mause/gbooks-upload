import os

from click.testing import CliRunner
from pytest import mark

from gbooks_upload import main as upload

os.environ["TERM"] = "dumb"


@mark.parametrize("subcommand", (None, "books", "shelves"))
def test_hello_world(snapshot, subcommand):
    runner = CliRunner()
    result = runner.invoke(upload, ([subcommand] if subcommand else []) + ["--help"])
    assert result.exit_code == 0
    assert result.output == snapshot
