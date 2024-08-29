#!/bin/bash

pushd backend
uvicorn app.main:app --reload --port 8000
popd
