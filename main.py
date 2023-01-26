# https://fastapi.tiangolo.com/tutorial/first-steps/
# To run locally:
#   Terminal: uvicorn main:app --reload
#   Browser: http://127.0.0.1:8000.
# Google Python modules:
#   pip install --upgrade \
#        google-auth \
#        google-api-python-client \
#        google-auth-httplib2 \
#        google-auth-oauthlib

import os
from datetime import datetime

import openai
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = FastAPI()

# allow any origin
origins = ["*"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"])

# load OPENAI_API_KEY from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# load Google Service Account Key and Scopes
GKEY_JSON = os.getenv("PATH_GOOGLE_SA_KEY_JSON")
GSCOPES = [
  "https://www.googleapis.com/auth/drive",
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/spreadsheets"]
# https://docs.google.com/spreadsheets/d/1-Httr306NaDwIIt8WKvYewKvJ2K_oEGh8FonJZpFLHA/edit#gid=0
GSHEET_ID = "1-Httr306NaDwIIt8WKvYewKvJ2K_oEGh8FonJZpFLHA"
GSHEET_RANGE = "data!A2:D3"


def add_q_a(q: str, a: str, client_ip: str) -> None:
  """Add question & answer to Google Sheet.

  Appends to the sheet.
  """
  # TODO: add time to process the question

  try:
    creds = service_account.Credentials.from_service_account_file(
      GKEY_JSON,).with_scopes(GSCOPES)
    service = build(
      "sheets", "v4",
      credentials = creds)

    # TODO: sanitize q & a from quotes, etc
    data = {"values": [[
      client_ip,
      datetime.now().strftime("%Y-%d-%m %H:%M:%S"),
      q,
      a ]]}

    service.spreadsheets().values().append(
      spreadsheetId=GSHEET_ID,
      body=data,
      range="A1:D2",
      valueInputOption="USER_ENTERED").execute()

  except HttpError as err:
    raise err


@app.get("/")
async def root() -> RedirectResponse:
  """API root."""
  return RedirectResponse(url="/docs")


@app.get("/answer")
def answer(question: str, request: Request) -> str:
    """Query OpenAI with a question and return the response."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens=709,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    answer = response.choices[0].text.strip()
    add_q_a(question, answer, request.client.host)
    
    return answer
