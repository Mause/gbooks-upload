# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: definitions/get_player.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1c\x64\x65\x66initions/get_player.proto"\x80\x01\n\x0eGetPlayerProto\x12"\n\x04\x66orm\x18\x02 \x01(\x0b\x32\x14.GetPlayerProto.Form\x1aJ\n\x04\x46orm\x12-\n\x05query\x18\x85\xf2\xc3\x90\x01 \x01(\x0b\x32\x1a.GetPlayerProto.Form.Query\x1a\x13\n\x05Query\x12\n\n\x02id\x18\x01 \x01(\tb\x06proto3'
)


_GETPLAYERPROTO = DESCRIPTOR.message_types_by_name["GetPlayerProto"]
_GETPLAYERPROTO_FORM = _GETPLAYERPROTO.nested_types_by_name["Form"]
_GETPLAYERPROTO_FORM_QUERY = _GETPLAYERPROTO_FORM.nested_types_by_name["Query"]
GetPlayerProto = _reflection.GeneratedProtocolMessageType(
    "GetPlayerProto",
    (_message.Message,),
    {
        "Form": _reflection.GeneratedProtocolMessageType(
            "Form",
            (_message.Message,),
            {
                "Query": _reflection.GeneratedProtocolMessageType(
                    "Query",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _GETPLAYERPROTO_FORM_QUERY,
                        "__module__": "definitions.get_player_pb2",
                        # @@protoc_insertion_point(class_scope:GetPlayerProto.Form.Query)
                    },
                ),
                "DESCRIPTOR": _GETPLAYERPROTO_FORM,
                "__module__": "definitions.get_player_pb2",
                # @@protoc_insertion_point(class_scope:GetPlayerProto.Form)
            },
        ),
        "DESCRIPTOR": _GETPLAYERPROTO,
        "__module__": "definitions.get_player_pb2",
        # @@protoc_insertion_point(class_scope:GetPlayerProto)
    },
)
_sym_db.RegisterMessage(GetPlayerProto)
_sym_db.RegisterMessage(GetPlayerProto.Form)
_sym_db.RegisterMessage(GetPlayerProto.Form.Query)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GETPLAYERPROTO._serialized_start = 33
    _GETPLAYERPROTO._serialized_end = 161
    _GETPLAYERPROTO_FORM._serialized_start = 87
    _GETPLAYERPROTO_FORM._serialized_end = 161
    _GETPLAYERPROTO_FORM_QUERY._serialized_start = 142
    _GETPLAYERPROTO_FORM_QUERY._serialized_end = 161
# @@protoc_insertion_point(module_scope)
