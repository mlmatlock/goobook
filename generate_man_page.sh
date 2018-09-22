#!/bin/sh

set -e
mkdir -p build
rst2man.py --strict goobook.1.rst build/goobook.1
echo Generated: build/goobook.1
