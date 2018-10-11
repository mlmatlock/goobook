#!/bin/sh

# Run static code analyis
# You need to have done: pipenv install --dev

# prospector is configured in .prospector.yaml

exec pipenv run prospector "$@"
