import json
from pathlib import Path

from google.protobuf.json_format import MessageToDict

from google_internal_apis.input_pb2 import LibraryDocumentResponse, TagsResponse
from google_internal_apis.json_format import dump, parse

HERE = Path(__file__).parent


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
    with open(HERE / "complex.json") as f:
        payload = json.load(f)
    out = parse(payload, LibraryDocumentResponse())
    assert str(out).strip() == snapshot
    assert MessageToDict(out) == snapshot

    # TODO: roundtrip test
