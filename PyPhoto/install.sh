#!/bin/bash
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
cd src/resources/
npm i
cd ..
cd ..