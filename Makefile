.PHONY: docs

all: clean install migrate run

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' -delete

flake8:
	flake8 --exclude=migrations,tests src

install:
	pip install .
	pip install -e .[test]

isort:
	isort --recursive --check-only --diff src tests

lint: flake8 isort

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

test:
	py.test tests
