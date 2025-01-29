import os
from os.path import basename
from pathlib import Path
from urllib.request import urlretrieve

from click.testing import CliRunner
from pytest import fixture

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
    assert result.output == snapshot


@fixture
def happy_epub(tmp_path):
    url = "https://github.com/IDPF/epub3-samples/releases/download/20230704/accessible_epub_3.epub"
    return get_epub(tmp_path, url)


def get_epub(tmp_path: Path, url: str) -> Path:
    out = tmp_path / basename(url)
    urlretrieve(url, out)
    return out


def test_upload(snapshot, betamax_session, monkeypatch, happy_epub):
    runner = CliRunner()
    monkeypatch.setattr("requests.Session", lambda: betamax_session)
    result = runner.invoke(upload, ["upload", str(happy_epub), "--bookshelf", "test"])
    assert result.exit_code == 0
    assert result.output == snapshot
