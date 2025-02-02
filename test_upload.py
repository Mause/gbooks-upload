import json
import os

from click.testing import CliRunner
from google.protobuf.json_format import MessageToDict

from gbooks_upload import main as upload
from gbooks_upload.endpoints import parse
from google_internal_apis.json_format import dump
from input_pb2 import LibraryDocumentResponse, TagsResponse

os.environ["TERM"] = "dumb"


def test_hello_world(snapshot):
    runner = CliRunner()
    result = runner.invoke(upload, ["--help"])
    assert result.exit_code == 0
    assert result.output == snapshot


def test_protoc(snapshot):
    original = [
        [
            ["tag_name_1", "tag_id_1", "1"],
            ["tag_name_2", "tag_id_2", "2"],
        ],
        [
            ["book_id_1", "tag_id_1", "1"],
            ["book_id_2", "tag_id_2", "2"],
        ],
    ]
    out = parse(
        original,
        TagsResponse(),
    )
    assert str(out).strip() == snapshot
    assert MessageToDict(out) == snapshot

    assert dump(out) == original


def test_parse_complex(snapshot):
    with open("complex.json") as f:
        payload = json.load(f)
    out = parse(payload, LibraryDocumentResponse())
    assert str(out).strip() == snapshot
    assert MessageToDict(out) == snapshot
