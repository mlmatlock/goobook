#!/bin/sh

# Format code
# You need to have done: poetry install --dev

poetry run black .
poetry run isort .