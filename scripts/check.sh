#!/bin/sh

# Run static code analysis
# You need to have done: poetry install --dev

# prospector is configured in prospector.yaml
poetry run prospector "$@"
