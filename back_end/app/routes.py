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
    # try:
        credentials = flow.step2_exchange(request.args.get('code'))
        userData = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=' + credentials.access_token).content
        userData = json.loads(userData.decode('utf-8'))
        user = {
            'name': userData['name'],
            'email': userData['email'],
            'googleId': userData['id']
        }
        olduser = models.User.query.filter(models.User.email == userData['email']).all()
        if olduser:
            return render_template('index.html', title="Calendar", user=userData['name'])
        else:
            insertUser = models.User(**user)
            db.session.add(insertUser)
            db.session.commit()
            return render_template('index.html', title="Calendar", user=userData['name'])
    # except:
    #     return render_template('login.html')

@app.route('/calendar')
def calendar():
    events = models.Vacation.query.all()
    eventList = []
    for event in events:
        eventObject = {
            'title': 'userId ' + 'Vacation',
            'start': event.fromDate,
            'end': event.toDate
        }
        eventList.append(eventObject)
    print(eventList)
    resp = jsonify(eventList)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return resp

@app.route('/vacation_request', methods=['POST'])
def vacation_request():
    # date = {
    #     'fromDate': request.form['date-from'],
    #     'toDate': request.form['date-to'],
    #     'owner': '1'
    # }
    #insertDate = models.Vacation(**date)
    insertDate = models.Vacation(
        fromDate=request.form['date-from'],
        toDate=request.form['date-to'],
        user_id='1'
    )
    db.session.add(insertDate)
    db.session.commit()

    resp = jsonify({'ok': 'ok'})
    resp.status_code = 200
    return resp