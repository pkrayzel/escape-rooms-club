#!/bin/sh
set -ex

# prepare s3 bucket for tests
aws --endpoint-url http://localstack:4572 s3 mb s3://scrapers-output

# site-downloader integration tests
pytest -vvvv /src/escape-rooms-club/site-downloader/tests/integration/
