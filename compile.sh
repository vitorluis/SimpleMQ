#!/usr/bin/env bash
python3 -m nuitka --recurse-all --standalone --recurse-directory=/usr/local/lib/python3.6/dist-packages/gevent \
--show-progress simplemq.py

cp config.yaml simplemq.dist
cp queues.json simplemq.dist
mkdir -p simplemq.dist/config