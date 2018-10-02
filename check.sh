#!/bin/sh
#exec flake8 --max-line-length=120 goobook
#exec pipenv run prospector --with-tool pyroma --with-tool vulture "$@"
exec pipenv run prospector "$@"

