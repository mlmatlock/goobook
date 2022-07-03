#!/bin/sh

# You need to have done: poetry install --dev

set -e
mkdir -p build
poetry run rst2man.py --strict goobook.1.rst build/goobook.1
echo Generated: build/goobook.1
