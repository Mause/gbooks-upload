import os

from click.testing import CliRunner

from gbooks_upload import main as upload
from gbooks_upload.endpoints import parse
from input_pb2 import TagsResponse

os.environ["TERM"] = "dumb"


def test_hello_world(snapshot):
    runner = CliRunner()
    result = runner.invoke(upload, ["--help"])
    assert result.exit_code == 0
    assert result.output == snapshot


def test_protoc(snapshot):
    assert parse([[["tag_name", "tag_id", 1]], []], TagsResponse()) == snapshot
