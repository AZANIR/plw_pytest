# Automation Framework with Playwright and pytest

## Setup local env
### To setup env in Windows run following PowerShell script:
```commandline
setup_venv.ps1
```

## Manual steps:
### 1. Install poetry:
Linux
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
Windows PowerShell
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

### 2. Create venv and activate it:

Windows
```bash
python -m venv venv
venv\Scripts\Activate.ps1''
```
Linux
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install requirements:
```bash
pip install -r requirements.txt
```