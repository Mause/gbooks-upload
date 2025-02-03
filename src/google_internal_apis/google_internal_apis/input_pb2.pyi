from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ["name", "tag_id", "created_at"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., tag_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Tagged(_message.Message):
    __slots__ = ["book_id", "tag_id", "tagged_at"]
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_AT_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    tag_id: str
    tagged_at: _timestamp_pb2.Timestamp
    def __init__(self, book_id: _Optional[str] = ..., tag_id: _Optional[str] = ..., tagged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TagsResponse(_message.Message):
    __slots__ = ["tags", "tagged_items"]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TAGGED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    tagged_items: _containers.RepeatedCompositeFieldContainer[Tagged]
    def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., tagged_items: _Optional[_Iterable[_Union[Tagged, _Mapping]]] = ...) -> None: ...

class TagRequest(_message.Message):
    __slots__ = ["tagged_items"]
    TAGGED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    tagged_items: _containers.RepeatedCompositeFieldContainer[Tagged]
    def __init__(self, tagged_items: _Optional[_Iterable[_Union[Tagged, _Mapping]]] = ...) -> None: ...

class LibraryDocumentResponse(_message.Message):
    __slots__ = ["library_documents"]
    LIBRARY_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    library_documents: LibraryDocument
    def __init__(self, library_documents: _Optional[_Union[LibraryDocument, _Mapping]] = ...) -> None: ...

class LibraryDocument(_message.Message):
    __slots__ = ["book_id", "book"]
    class Book(_message.Message):
        __slots__ = ["title", "authors", "publisher", "published_date", "description", "page_count", "version", "cover_images", "language", "url", "unknown1", "unknown2s", "unknown3", "unknown4", "series", "unknown5s", "unknown6", "geos", "unknown7", "rating", "genres"]
        class BookGenre(_message.Message):
            __slots__ = ["genre"]
            GENRE_FIELD_NUMBER: _ClassVar[int]
            genre: LibraryDocument.Book.Genre
            def __init__(self, genre: _Optional[_Union[LibraryDocument.Book.Genre, _Mapping]] = ...) -> None: ...
        class Geo(_message.Message):
            __slots__ = ["geo", "geo_id"]
            GEO_FIELD_NUMBER: _ClassVar[int]
            GEO_ID_FIELD_NUMBER: _ClassVar[int]
            geo: str
            geo_id: str
            def __init__(self, geo: _Optional[str] = ..., geo_id: _Optional[str] = ...) -> None: ...
        class Genre(_message.Message):
            __slots__ = ["genre", "subgenre"]
            GENRE_FIELD_NUMBER: _ClassVar[int]
            SUBGENRE_FIELD_NUMBER: _ClassVar[int]
            genre: str
            subgenre: str
            def __init__(self, genre: _Optional[str] = ..., subgenre: _Optional[str] = ...) -> None: ...
        class Rating(_message.Message):
            __slots__ = ["rating", "number_of_reviews"]
            RATING_FIELD_NUMBER: _ClassVar[int]
            NUMBER_OF_REVIEWS_FIELD_NUMBER: _ClassVar[int]
            rating: float
            number_of_reviews: str
            def __init__(self, rating: _Optional[float] = ..., number_of_reviews: _Optional[str] = ...) -> None: ...
        class Series(_message.Message):
            __slots__ = ["this_book_title", "series", "book_in_series"]
            THIS_BOOK_TITLE_FIELD_NUMBER: _ClassVar[int]
            SERIES_FIELD_NUMBER: _ClassVar[int]
            BOOK_IN_SERIES_FIELD_NUMBER: _ClassVar[int]
            this_book_title: str
            series: _containers.RepeatedCompositeFieldContainer[LibraryDocument.Book.SingleSeries]
            book_in_series: str
            def __init__(self, this_book_title: _Optional[str] = ..., series: _Optional[_Iterable[_Union[LibraryDocument.Book.SingleSeries, _Mapping]]] = ..., book_in_series: _Optional[str] = ...) -> None: ...
        class SingleSeries(_message.Message):
            __slots__ = ["series_id", "unknown1", "unknown2", "unknown3", "unknown4", "series_name"]
            SERIES_ID_FIELD_NUMBER: _ClassVar[int]
            UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
            UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
            UNKNOWN3_FIELD_NUMBER: _ClassVar[int]
            UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
            SERIES_NAME_FIELD_NUMBER: _ClassVar[int]
            series_id: str
            unknown1: int
            unknown2: int
            unknown3: _wrappers_pb2.StringValue
            unknown4: int
            series_name: str
            def __init__(self, series_id: _Optional[str] = ..., unknown1: _Optional[int] = ..., unknown2: _Optional[int] = ..., unknown3: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., unknown4: _Optional[int] = ..., series_name: _Optional[str] = ...) -> None: ...
        class CoverImage(_message.Message):
            __slots__ = ["url", "scale", "color", "width", "height"]
            URL_FIELD_NUMBER: _ClassVar[int]
            SCALE_FIELD_NUMBER: _ClassVar[int]
            COLOR_FIELD_NUMBER: _ClassVar[int]
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            url: str
            scale: int
            color: str
            width: int
            height: int
            def __init__(self, url: _Optional[str] = ..., scale: _Optional[int] = ..., color: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        AUTHORS_FIELD_NUMBER: _ClassVar[int]
        PUBLISHER_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_DATE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        COVER_IMAGES_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN2S_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN3_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
        SERIES_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN5S_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN6_FIELD_NUMBER: _ClassVar[int]
        GEOS_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN7_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        GENRES_FIELD_NUMBER: _ClassVar[int]
        title: str
        authors: _containers.RepeatedScalarFieldContainer[str]
        publisher: str
        published_date: _date_pb2.Date
        description: str
        page_count: int
        version: str
        cover_images: _containers.RepeatedCompositeFieldContainer[LibraryDocument.Book.CoverImage]
        language: str
        url: str
        unknown1: int
        unknown2s: _containers.RepeatedScalarFieldContainer[int]
        unknown3: int
        unknown4: int
        series: LibraryDocument.Book.Series
        unknown5s: _containers.RepeatedScalarFieldContainer[int]
        unknown6: _wrappers_pb2.StringValue
        geos: _containers.RepeatedCompositeFieldContainer[LibraryDocument.Book.Geo]
        unknown7: _wrappers_pb2.StringValue
        rating: LibraryDocument.Book.Rating
        genres: _containers.RepeatedCompositeFieldContainer[LibraryDocument.Book.BookGenre]
        def __init__(self, title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., publisher: _Optional[str] = ..., published_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., description: _Optional[str] = ..., page_count: _Optional[int] = ..., version: _Optional[str] = ..., cover_images: _Optional[_Iterable[_Union[LibraryDocument.Book.CoverImage, _Mapping]]] = ..., language: _Optional[str] = ..., url: _Optional[str] = ..., unknown1: _Optional[int] = ..., unknown2s: _Optional[_Iterable[int]] = ..., unknown3: _Optional[int] = ..., unknown4: _Optional[int] = ..., series: _Optional[_Union[LibraryDocument.Book.Series, _Mapping]] = ..., unknown5s: _Optional[_Iterable[int]] = ..., unknown6: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., geos: _Optional[_Iterable[_Union[LibraryDocument.Book.Geo, _Mapping]]] = ..., unknown7: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., rating: _Optional[_Union[LibraryDocument.Book.Rating, _Mapping]] = ..., genres: _Optional[_Iterable[_Union[LibraryDocument.Book.BookGenre, _Mapping]]] = ...) -> None: ...
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    book: LibraryDocument.Book
    def __init__(self, book_id: _Optional[str] = ..., book: _Optional[_Union[LibraryDocument.Book, _Mapping]] = ...) -> None: ...
