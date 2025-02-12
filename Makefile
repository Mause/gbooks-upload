.PHONY: all clean

all: man/gbooks-upload.1
	cd src/google_internal_apis && make

clean:
	cd src/google_internal_apis && make clean


man/gbooks-upload.1:
	python -c '__import__("click_man.shell").shell.cli()' gbooks-upload --man-version 0.1.0
