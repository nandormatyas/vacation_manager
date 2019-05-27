import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ['headers', 'cookies', 'json']
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_REFRESH_COOKIE_PATH = '/token/refresh'
    JWT_COOKIE_CSRF_PROTECT = False

#  Configure application to store JWTs in cookies. Whenever you make
# # a request to a protected endpoint, you will need to send in the
# # access or refresh JWT via a cookie.
# app.config['JWT_TOKEN_LOCATION'] = ['cookies']

# # Set the cookie paths, so that you are only sending your access token
# # cookie to the access endpoints, and only sending your refresh token
# # to the refresh endpoint. Technically this is optional, but it is in
# # your best interest to not send additional cookies in the request if
# # they aren't needed.
# app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
# app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'

# # Disable CSRF protection for this example. In almost every case,
# # this is a bad idea. See examples/csrf_protection_with_cookies.py
# # for how safely store JWTs in cookies
# app.config['JWT_COOKIE_CSRF_PROTECT'] = False
