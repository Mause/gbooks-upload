import warnings
from pprint import pformat

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import StringValue


def dump(message):
    if isinstance(message, Timestamp):
        return str(message.ToMilliseconds())
    if isinstance(message, StringValue):
        return message.value
    fields = message.DESCRIPTOR.fields
    arrays = []
    for field in fields:
        if field.label == field.LABEL_REPEATED:
            if field.type == field.TYPE_MESSAGE:
                arrays.append([dump(item) for item in getattr(message, field.name)])
            else:
                arrays.append(getattr(message, field.name))
        elif field.label == field.LABEL_REQUIRED:
            if field.type == field.TYPE_MESSAGE:
                arrays.append(dump(getattr(message, field.name)))
            else:
                arrays.append(getattr(message, field.name))
        elif field.label == field.LABEL_OPTIONAL:
            if field.type == field.TYPE_MESSAGE:
                arrays.append(dump(getattr(message, field.name)))
            else:
                arrays.append(getattr(message, field.name))
        else:
            raise ValueError("Unknown label")
    return arrays


def repeated(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        for array in value:
            parse(array, getattr(message, field.name).add())
    else:
        getattr(message, field.name).extend(value)


def required(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        parse(value, getattr(message, field.name))
    else:
        setattr(message, field.name, value)


def optional(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        parse(value, getattr(message, field.name))
    else:
        setattr(message, field.name, value)


def parse(arrays, message):
    fields = message.DESCRIPTOR.fields
    if isinstance(message, Timestamp):
        message.FromMilliseconds(int(arrays))
        return message
    if isinstance(message, StringValue):
        if arrays:
            message.MergeFromString(arrays)
        return message

    for field in fields:
        match field.label:
            case field.LABEL_REPEATED:
                value = arrays[field.number - 1]
                repeated(message, field, value)
            case field.LABEL_REQUIRED:
                value = arrays[field.number - 1]
                required(message, field, value)
            case field.LABEL_OPTIONAL:
                if len(arrays) >= field.number:
                    value = arrays[field.number - 1]
                    optional(message, field, value)
            case _:
                raise ValueError("Unknown label")
    remaining = arrays[fields[-1].number :]
    if remaining:
        warnings.warn("Extra fields: " + pformat(remaining))
    return message
