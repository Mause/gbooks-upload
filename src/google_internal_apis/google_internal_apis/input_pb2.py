# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google_internal_apis/input.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google_internal_apis/input.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"S\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06tag_id\x18\x02 \x02(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"X\n\x06Tagged\x12\x0f\n\x07\x62ook_id\x18\x01 \x02(\t\x12\x0e\n\x06tag_id\x18\x02 \x02(\t\x12-\n\ttagged_at\x18\x03 \x02(\x0b\x32\x1a.google.protobuf.Timestamp\"A\n\x0cTagsResponse\x12\x12\n\x04tags\x18\x01 \x03(\x0b\x32\x04.Tag\x12\x1d\n\x0ctagged_items\x18\x02 \x03(\x0b\x32\x07.Tagged\"+\n\nTagRequest\x12\x1d\n\x0ctagged_items\x18\x01 \x03(\x0b\x32\x07.Tagged\"F\n\x17LibraryDocumentResponse\x12+\n\x11library_documents\x18\x01 \x02(\x0b\x32\x10.LibraryDocument\"\xc0\t\n\x0fLibraryDocument\x12\x0f\n\x07\x62ook_id\x18\x01 \x02(\t\x12#\n\x04\x62ook\x18\x02 \x02(\x0b\x32\x15.LibraryDocument.Book\x1a\xf6\x08\n\x04\x42ook\x12\r\n\x05title\x18\x01 \x02(\t\x12\x0f\n\x07\x61uthors\x18\x02 \x03(\t\x12\x11\n\tpublisher\x18\x03 \x02(\t\x12\x16\n\x0epublished_date\x18\x04 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x02(\t\x12\x12\n\npage_count\x18\x06 \x02(\x05\x12\x0f\n\x07version\x18\x07 \x02(\t\x12\x36\n\x0c\x63over_images\x18\x08 \x03(\x0b\x32 .LibraryDocument.Book.CoverImage\x12\x10\n\x08language\x18\t \x02(\t\x12\x0b\n\x03url\x18\n \x02(\t\x12\x10\n\x08unknown1\x18\x0b \x02(\x05\x12\x11\n\tunknown2s\x18\x0c \x03(\x05\x12\x10\n\x08unknown3\x18\r \x02(\x05\x12\x10\n\x08unknown4\x18\x0e \x02(\x05\x12,\n\x06series\x18\x0f \x02(\x0b\x32\x1c.LibraryDocument.Book.Series\x12\x11\n\tunknown5s\x18\x10 \x03(\x05\x12.\n\x08unknown6\x18\x11 \x02(\x0b\x32\x1c.google.protobuf.StringValue\x12\'\n\x04geos\x18\x12 \x03(\x0b\x32\x19.LibraryDocument.Book.Geo\x12.\n\x08unknown7\x18\x13 \x02(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06rating\x18\x14 \x02(\x0b\x32\x1c.LibraryDocument.Book.Rating\x12/\n\x06genres\x18\x15 \x03(\x0b\x32\x1f.LibraryDocument.Book.BookGenre\x1a\x37\n\tBookGenre\x12*\n\x05genre\x18\x01 \x02(\x0b\x32\x1b.LibraryDocument.Book.Genre\x1a\"\n\x03Geo\x12\x0b\n\x03geo\x18\x01 \x02(\t\x12\x0e\n\x06geo_id\x18\x02 \x02(\t\x1a(\n\x05Genre\x12\r\n\x05genre\x18\x01 \x02(\t\x12\x10\n\x08subgenre\x18\x02 \x01(\t\x1a\x33\n\x06Rating\x12\x0e\n\x06rating\x18\x01 \x02(\x02\x12\x19\n\x11number_of_reviews\x18\x02 \x02(\t\x1am\n\x06Series\x12\x17\n\x0fthis_book_title\x18\x01 \x02(\t\x12\x32\n\x06series\x18\x02 \x03(\x0b\x32\".LibraryDocument.Book.SingleSeries\x12\x16\n\x0e\x62ook_in_series\x18\x03 \x02(\t\x1a\x9c\x01\n\x0cSingleSeries\x12\x11\n\tseries_id\x18\x01 \x02(\t\x12\x10\n\x08unknown1\x18\x02 \x02(\x05\x12\x10\n\x08unknown2\x18\x03 \x02(\x05\x12.\n\x08unknown3\x18\x04 \x02(\x0b\x32\x1c.google.protobuf.StringValue\x12\x10\n\x08unknown4\x18\x05 \x02(\x05\x12\x13\n\x0bseries_name\x18\x06 \x02(\t\x1aV\n\nCoverImage\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\r\n\x05scale\x18\x02 \x02(\x05\x12\r\n\x05\x63olor\x18\x03 \x02(\t\x12\r\n\x05width\x18\x04 \x02(\x05\x12\x0e\n\x06height\x18\x05 \x02(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google_internal_apis.input_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TAG']._serialized_start=101
  _globals['_TAG']._serialized_end=184
  _globals['_TAGGED']._serialized_start=186
  _globals['_TAGGED']._serialized_end=274
  _globals['_TAGSRESPONSE']._serialized_start=276
  _globals['_TAGSRESPONSE']._serialized_end=341
  _globals['_TAGREQUEST']._serialized_start=343
  _globals['_TAGREQUEST']._serialized_end=386
  _globals['_LIBRARYDOCUMENTRESPONSE']._serialized_start=388
  _globals['_LIBRARYDOCUMENTRESPONSE']._serialized_end=458
  _globals['_LIBRARYDOCUMENT']._serialized_start=461
  _globals['_LIBRARYDOCUMENT']._serialized_end=1677
  _globals['_LIBRARYDOCUMENT_BOOK']._serialized_start=535
  _globals['_LIBRARYDOCUMENT_BOOK']._serialized_end=1677
  _globals['_LIBRARYDOCUMENT_BOOK_BOOKGENRE']._serialized_start=1133
  _globals['_LIBRARYDOCUMENT_BOOK_BOOKGENRE']._serialized_end=1188
  _globals['_LIBRARYDOCUMENT_BOOK_GEO']._serialized_start=1190
  _globals['_LIBRARYDOCUMENT_BOOK_GEO']._serialized_end=1224
  _globals['_LIBRARYDOCUMENT_BOOK_GENRE']._serialized_start=1226
  _globals['_LIBRARYDOCUMENT_BOOK_GENRE']._serialized_end=1266
  _globals['_LIBRARYDOCUMENT_BOOK_RATING']._serialized_start=1268
  _globals['_LIBRARYDOCUMENT_BOOK_RATING']._serialized_end=1319
  _globals['_LIBRARYDOCUMENT_BOOK_SERIES']._serialized_start=1321
  _globals['_LIBRARYDOCUMENT_BOOK_SERIES']._serialized_end=1430
  _globals['_LIBRARYDOCUMENT_BOOK_SINGLESERIES']._serialized_start=1433
  _globals['_LIBRARYDOCUMENT_BOOK_SINGLESERIES']._serialized_end=1589
  _globals['_LIBRARYDOCUMENT_BOOK_COVERIMAGE']._serialized_start=1591
  _globals['_LIBRARYDOCUMENT_BOOK_COVERIMAGE']._serialized_end=1677
# @@protoc_insertion_point(module_scope)
