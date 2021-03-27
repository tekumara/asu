MAKEFLAGS += --warn-undefined-variables
SHELL = /bin/bash -o pipefail
.DEFAULT_GOAL := help
.PHONY: help install check lint pyright test hooks install-hooks dist publish

## display help message
help:
	@awk '/^##.*$$/,/^[~\/\.0-9a-zA-Z_-]+:/' $(MAKEFILE_LIST) | awk '!(NR%2){print $$0p}{p=$$0}' | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | sort

venv = venv
pip := $(venv)/bin/pip

$(pip):
	# create empty virtualenv containing pip
	$(if $(value VIRTUAL_ENV),$(error Cannot create a virtualenv when running in a virtualenv. Please deactivate the current virtual env $(VIRTUAL_ENV)),)
	python3 -m venv --clear $(venv)
	$(pip) install wheel

$(venv): setup.py $(pip)
	$(pip) install -e '.[dev]'
	touch $(venv)

## create venv and install this package and hooks
install: $(venv) node_modules $(if $(value CI),,install-hooks)

## format all code
format: $(venv)
	$(venv)/bin/autopep8 .
	$(venv)/bin/isort .

## lint code and run static type check
check: lint pyright

## lint using flake8
lint: $(venv)
	$(venv)/bin/flake8

node_modules: package.json
	npm install
	touch node_modules

## pyright
pyright: node_modules $(venv)
	source $(venv)/bin/activate && node_modules/.bin/pyright

## run tests
test: $(venv)
	$(venv)/bin/pytest

## build distribution
dist: $(venv)
	rm -rf dist/*
	$(venv)/bin/python setup.py sdist
	$(venv)/bin/python setup.py bdist_wheel

## publish to pypi
publish: $(venv)
	$(venv)/bin/twine upload dist/*

## run pre-commit git hooks on all files
hooks: install-hooks $(venv)
	$(venv)/bin/pre-commit run --all-files --hook-stage push

install-hooks: .git/hooks/pre-commit .git/hooks/pre-push

.git/hooks/pre-commit: $(venv)
	$(venv)/bin/pre-commit install -t pre-commit

.git/hooks/pre-push: $(venv)
	$(venv)/bin/pre-commit install -t pre-push
