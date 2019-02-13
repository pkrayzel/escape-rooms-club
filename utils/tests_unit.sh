#!/bin/sh
set -ex

# site-downloader unit tests
pytest -vvvv /src/escape-rooms-club/site-downloader/tests/unit/
