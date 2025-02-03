from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DummyMessage(_message.Message):
    __slots__ = ["dummy_field"]
    DUMMY_FIELD_FIELD_NUMBER: _ClassVar[int]
    dummy_field: _wrappers_pb2.StringValue
    def __init__(self, dummy_field: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
