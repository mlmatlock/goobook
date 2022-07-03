#!/bin/sh

# Run static code analyis
# You need to have done: poetry install --dev

# prospector is configured in .prospector.yaml

exec poetry run prospector "$@"
