all: google_internal_apis/input_pb2.py google_internal_apis/endpoints.py


google_internal_apis/endpoints.py: endpoints.yaml genny.py
	python genny.py


PURELIB=$(shell python -c "import sysconfig; print(sysconfig.get_paths()['purelib'])")

%_pb2.py: %.proto
	protoc --python_out=. $< --proto_path=/usr/include --proto_path=. --proto_path=$(PURELIB)
