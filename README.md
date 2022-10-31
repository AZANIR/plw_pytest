# Automation Framework with Playwright and pytest

## Manual steps:
### 1. Install environment:

```bash
run: |
  python -m pip install --upgrade pip
  pip install pipenv
  pipenv install --system
  playwright install chromium
```

### 2. Run playwright tests:
reopen terminal and run:
```bash
pytest
```

### 3. Run allure report:
```bash
allure serve reports
```

### 4. To run tests with HTML report:
```bash
pytest --template=html1/index.html --report=report.html
```