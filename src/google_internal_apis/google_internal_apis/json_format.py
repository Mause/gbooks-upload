from google.protobuf.timestamp_pb2 import Timestamp


def dump(message):
    if isinstance(message, Timestamp):
        return str(message.ToMilliseconds())
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
