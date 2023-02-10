#!/bin/sh
set -x -e

# ruff
ruff check .

# black
black --check .

# mypy
mypy .

# pytest
pytest .
