
# Simple Python Web App

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Run with Docker

```bash
docker build -t simple-python-webapp .
docker run -p 5000:5000 simple-python-webapp
```

Or:

```bash
docker compose up --build
```
