import os
from oauth2client.client import OAuth2WebServerFlow

basedir = os.path.abspath(os.path.dirname(__file__))

def flow_config():

  return OAuth2WebServerFlow(client_id=os.environ.get('CLIENT_ID'),
                        client_secret=os.environ.get('CLIENT_SECRET'),
                        scope=['https://www.googleapis.com/auth/gmail.readonly',
                                'https://www.googleapis.com/auth/userinfo.profile',
                                'https://www.googleapis.com/auth/userinfo.email' ],
                        redirect_uri='http://localhost:5000/google_auth')
