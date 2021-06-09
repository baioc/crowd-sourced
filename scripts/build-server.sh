#!/bin/sh

cd server
docker build -t dotnetapiserver . --no-
docker cp data/encodings.csv dotnetapiserver:/app/encodings.csv