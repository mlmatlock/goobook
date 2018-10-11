#!/bin/sh

# You need to have done: pipenv install --dev

set -e
mkdir -p build
pipenv run rst2man.py --strict goobook.1.rst build/goobook.1
echo Generated: build/goobook.1
