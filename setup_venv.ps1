(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

python -m venv venv

venv\Scripts\Activate.ps1

pip install -r requirements.txt
