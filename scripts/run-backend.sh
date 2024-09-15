#!/bin/bash

# builds python backend
pushd python-backend
# Check if running on Windows (Git Bash) or Linux/Mac
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows path for venv activation
    source venv/Scripts/activate
else
    # Linux/Mac path for venv activation
    source venv/bin/activate
fi

uvicorn app.main:app --host 0.0.0.0 --reload --port 8000
popd
