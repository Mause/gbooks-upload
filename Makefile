.PHONY: all clean

all: man/gbooks-upload.1
	cd src/google_internal_apis && make

clean:
	rm -f man/*
	cd src/google_internal_apis && make clean


man/gbooks-upload.1:
	python .github/workflows/generate-man.py
