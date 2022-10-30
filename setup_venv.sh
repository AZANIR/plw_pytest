curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

export PATH="$HOME/.poetry/bin:$PATH"

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
