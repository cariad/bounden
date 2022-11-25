#!/bin/bash

set -euo pipefail

echo "${1:?}" > bounden/VERSION

rm -rf dist
python setup.py bdist_wheel
rm -rf build
