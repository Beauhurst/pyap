#!/bin/sh
set -x -e

# ruff
ruff check .

# black
black --check .

# mypy
mypy -m pyap_beauhurst

# pytest
pytest .
