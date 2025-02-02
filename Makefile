all: google_internal_apis/google_internal_apis/endpoints.py


google_internal_apis/google_internal_apis/endpoints.py: google_internal_apis/endpoints.yaml google_internal_apis/genny.py
	python google_internal_apis/genny.py
