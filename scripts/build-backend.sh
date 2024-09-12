pushd python-backend

rm -rf venv
python -m venv venv
# Check if running on Windows (Git Bash) or Linux/Mac
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows path for venv activation
    source venv/Scripts/activate
else
    # Linux/Mac path for venv activation
    source venv/bin/activate
fi

pip install --upgrade pip
pip install python-dotenv
pip install -r requirements.txt

popd

pushd nodejs-backend
rm -rf node_modules
npm i
popd