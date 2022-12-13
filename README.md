# api

Source:
* [Using FastAPI to Build Python Web APIs – Real Python](https://realpython.com/fastapi-python-web-apis/)

## Python setup

On Mac Terminal:

```bash

# check version of python
which python3
# /opt/homebrew/bin/python3
python3 --version
# Python 3.10.8

# upgrade pip
python3 -m pip install --upgrade pip

# install modules
python3 -m pip install --upgrade fastapi
python3 -m pip install --upgrade uvicorn
python3 -m pip install --upgrade python-dotenv
```

## Run locally

```bash
cd ~/Github/cstories-app/api
uvicorn main:app --reload
```