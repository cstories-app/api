from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import openai
from dotenv import load_dotenv

app = FastAPI()

# allow any origin
origins = ["*"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# load OPENAI_API_KEY from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
async def root():
  return RedirectResponse(url='/docs')

@app.get("/answer")
def answer(question: str):
  response = openai.Completion.create(
    engine            = "text-davinci-003",
    prompt            = question,
    temperature       = 0.7,
    max_tokens        = 709,
    top_p             = 1,
    frequency_penalty = 0,
    presence_penalty  = 0)
  return(response.choices[0].text)
