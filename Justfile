make:
    protoc --purerpc_out=. --python_out=. -I. greeter.proto
