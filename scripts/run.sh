#!/bin/bash

pushd backend
uvicorn app.main:app --host 0.0.0.0 --reload --port 8000
popd
