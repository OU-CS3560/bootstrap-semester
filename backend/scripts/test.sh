#!/bin/sh

set -e
set -x

python -m pytest app/tests "${@}"
