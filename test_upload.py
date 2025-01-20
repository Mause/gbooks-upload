import os
from zipfile import ZipFile

from click.testing import CliRunner

from upload import main as upload

os.environ["TERM"] = "dumb"


def test_hello_world(snapshot):
    runner = CliRunner()
    result = runner.invoke(upload, ["--help"])
    assert result.exit_code == 0
    assert result.output == snapshot


def test_non_existing_file(snapshot):
    runner = CliRunner()
    result = runner.invoke(upload, ["upload", "dummy.epub"])
    assert result.exit_code == 2


def test_upload(snapshot, betamax_session):
    runner = CliRunner()
    with runner.isolated_filesystem():
        with ZipFile("dummy.epub", "w") as f:
            f.writestr("dummy", "dummy")
        result = runner.invoke(upload, ["upload", "dummy.epub"])
        assert result.exit_code == 0
        assert result.output == snapshot
