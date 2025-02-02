all: src/google_internal_apis/google_internal_apis/endpoints.py

src/google_internal_apis/google_internal_apis/endpoints.py: src/google_internal_apis/endpoints.yaml src/google_internal_apis/genny.py
	python src/google_internal_apis/genny.py
