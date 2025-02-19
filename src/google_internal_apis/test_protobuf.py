import json
from pathlib import Path
from unittest.mock import Mock
from urllib.parse import urlparse, urlunparse

from ghunt.helpers.auth import GHuntCreds
from google.protobuf.json_format import MessageToDict
from google.protobuf.wrappers_pb2 import StringValue
from httpx import AsyncClient
from pytest import mark, raises
from vcr import VCR

from google_internal_apis.dummy_pb2 import DummyMessage
from google_internal_apis.endpoints import WaaRpc
from google_internal_apis.input_pb2 import LibraryDocumentResponse, TagsResponse
from google_internal_apis.json_format import dump, parse

HERE = Path(__file__).parent


@mark.asyncio
async def test_case():
    def filt(r):
        r.headers.pop("Cookie", None)
        r.headers.pop("Authorization", None)

        url = urlparse(r.uri)
        r.uri = urlunparse(
            (
                url.scheme,
                url.netloc,
                url.path,
                url.params,
                "",  # url.query,
                url.fragment,
            )
        )

        return r

    with VCR(before_record_request=filt).use_cassette("test_case.yaml"):
        creds = Mock(spec=GHuntCreds)
        creds.are_creds_loaded.return_value = True
        creds.cookies = {"SAPISID": "test"}
        client = WaaRpc(creds, AsyncClient())

        with raises(Exception, match="Request is missing required authentication credential."):
            await client.ping()


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


def test_string_value():
    assert parse([None], DummyMessage()) == DummyMessage()
    assert parse(["test"], DummyMessage()) == DummyMessage(
        dummy_field=StringValue(value="test")
    )

    assert dump(DummyMessage(dummy_field=StringValue(value="test")))[0] == "test"
    assert dump(DummyMessage())[0] is None
