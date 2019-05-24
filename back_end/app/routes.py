from app import app, db
import requests
import os
import json
from . import models
from flask import jsonify
from flask import render_template
from flask_cors import CORS
from flask import request, redirect
from oauth2client.client import OAuth2WebServerFlow

CORS(app)

flow = OAuth2WebServerFlow(client_id=os.environ.get('CLIENT_ID'),
                        client_secret=os.environ.get('CLIENT_SECRET'),
                        scope=['https://www.googleapis.com/auth/gmail.readonly',
                                'https://www.googleapis.com/auth/userinfo.profile',
                                'https://www.googleapis.com/auth/userinfo.email' ],
                        redirect_uri='http://localhost:5000/index')
@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/google_login', methods=['POST'])
def google_login():

    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)

@app.route('/index')
def index():
    #try:
        credentials = flow.step2_exchange(request.args.get('code'))
        userData = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=' + credentials.access_token).content
        userData = json.loads(userData.decode('utf-8'))
        user = {
            'name': userData['name'],
            'email': userData['email'],
            'googleId': userData['id']
        }
        if models.User.Select.where(email = userData['email']):
            print('USERINHERE')
        else:
            insertUser = models.User(**user)
            db.session.add(insertUser)
            db.session.commit()
        return render_template('index.html', title="Calendar")
    # except:
    #     return render_template('login.html')

@app.route('/calendar')
def calendar():
    events = [
            {
                'title': 'All Day Event',
                'start': '2018-01-01',
            },
            {
                'title': 'Long Event',
                'start': '2018-01-07',
                'end': '2018-01-10'
            },
            {
                'id': '999',
                'title': 'Repeating Event',
                'start': '2018-01-09T16:00:00'
            },
            {
                'id': '999',
                'title': 'Repeating Event',
                'start': '2018-01-16T16:00:00'
            },
            {
                'title': 'Conference',
                'start': '2018-01-11',
                'end': '2018-01-13'
            },
            {
                'title': 'Meeting',
                'start': '2018-01-12T10:30:00',
                'end': '2018-01-12T12:30:00'
            },
            {
                'title': 'Lunch',
                'start': '2018-01-12T12:00:00'
            },
            {
                'title': 'Meeting',
                'start': '2018-01-12T14:30:00'
            },
            {
                'title': 'Happy Hour',
                'start': '2018-01-12T17:30:00'
            },
            {
                'title': 'Dinner',
                'start': '2018-01-12T20:00:00'
            },
            {
                'title': 'Birthday Party',
                'start': '2018-01-13T07:00:00'
            },
            {
                'title': 'Click for Google',
                'url': 'http://google.com/',
                'start': '2018-01-28'
            }
            ]

    resp = jsonify(events)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return resp

@app.route('/vacation_request', methods=['POST'])
def vacation_request():
    resp = jsonify({'ok': 'ok'})
    resp.status_code = 200
    return resp