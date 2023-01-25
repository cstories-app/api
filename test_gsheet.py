# background: [log request & response with middleware to fastapi · Issue #2 · cstories-app/api](https://github.com/cstories-app/api/issues/2)
# install dependencies:
#   https://developers.google.com/sheets/api/quickstart/python
#   pip install --upgrade google-authgoogle-api-python-client google-auth-httplib2 google-auth-oauthlib 
#   pip3.11 install --upgrade google-auth google-api-python-client google-auth-httplib2 google-auth-oauthlib 
# [q&a - cstories.app/beta - Google Sheets](https://docs.google.com/spreadsheets/d/1-Httr306NaDwIIt8WKvYewKvJ2K_oEGh8FonJZpFLHA/edit#gid=0)
#   - created gsheet in cstories Gdrive
#   - shared with Google Service Account cstories-app-for-gsheets@cstories-app.iam.gserviceaccount.com
# and to work with service account
#  https://denisluiz.medium.com/python-with-google-sheets-service-account-step-by-step-8f74c26ed28e
# https://google-auth.readthedocs.io/en/master/user-guide.html


from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Google Service Account Key and Scopes
KEY_JSON = '/Users/bbest/My Drive/private/cstories-app-9a9b9e400bf2.json'
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]

# Google Sheet ID and range
GSHEET_ID = '1-Httr306NaDwIIt8WKvYewKvJ2K_oEGh8FonJZpFLHA'
GSHEET_RANGE = 'data!A2:D3'

def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """

  try:
    creds = service_account.Credentials.from_service_account_file(
      KEY_JSON).with_scopes(SCOPES)
    service = build(
      'sheets', 'v4', credentials=creds)

    data = {
      'values' : [['2023-01-25', 'what is up with 42?']] }

    response = service.spreadsheets().values().append(
      spreadsheetId    = GSHEET_ID, 
      body             = data, 
      range            = 'A1:D2', 
      valueInputOption = 'USER_ENTERED').execute()
    
  except HttpError as err:
    print(err)

if __name__ == '__main__':
    main()