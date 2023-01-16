#!/usr/bin/env bash

cd /root/tail-database-exporter
/usr/bin/python3 -m venv venv
. ./venv/bin/activate
python3 -u setup.py install

TAILDB_EXPORTER_OUTPUT_DIR=/root/.tail-database-exporter/mainnet python3 -u start.py
