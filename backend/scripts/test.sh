#!/bin/sh

set -e
set -x

pytest app/tests "${@}"
