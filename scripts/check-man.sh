#!/bin/sh

# You need to have done: poetry install --dev

set -e

mkdir -p build
echo Writing manpage to ./build/goobook.1
poetry run rst2man.py --strict goobook.1.rst build/goobook.1
