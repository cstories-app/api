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

Create `.env` file in same directory as `main.py` with 

```sh
# for ben@ecoquants.com
OPENAI_API_KEY=suPer$ecret!
```

Run the local web server

```bash
# change directory into folder containing main.py
cd ~/Github/cstories-app/api
# run local web server
uvicorn main:app --reload
```