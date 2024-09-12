#!/bin/bash

# builds python backend
pushd python-backend
source venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --reload --port 8000
popd
