import os

from click.testing import CliRunner

from gbooks_upload import main as upload

os.environ["TERM"] = "dumb"


def test_hello_world(snapshot):
    runner = CliRunner()
    result = runner.invoke(upload, ["--help"])
    assert result.exit_code == 0
    assert result.output == snapshot
