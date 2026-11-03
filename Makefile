.PHONY: install test coverage run build clean
   
install:
	python -m pip install -r requirements.lock

test:
	python -m pytest

coverage:
	python -m coverage run -m pytest && python -m coverage report -m

run:
	python -m uvicorn app.main:app --host 127.0.0.1 --port 8000

build:
	python -m build

clean:
	python -m pip cache purge
