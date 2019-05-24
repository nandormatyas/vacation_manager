from app import app, db
import requests
import os
import json
from . import models
from flask import jsonify, render_template, request, redirect
from flask_cors import CORS
from google_config import flow_config

CORS(app)

flow= flow_config()

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
    try:
        credentials = flow.step2_exchange(request.args.get('code'))
        userData = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=' + credentials.access_token).content
        userData = json.loads(userData.decode('utf-8'))
        olduser = models.User.query.filter(models.User.email == userData['email']).all()
        if olduser:
            return render_template('index.html', title="Calendar", user=userData['name'])
        else:
            user = {
                'name': userData['name'],
                'email': userData['email'],
                'googleId': userData['id']
            }
            insertUser = models.User(**user)
            db.session.add(insertUser)
            db.session.commit()
            return render_template('index.html', title="Calendar", user=userData['name'])
    except:
        return render_template('login.html')

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
    insertDate = models.Vacation(
        fromDate=request.form['date-from'],
        toDate=request.form['date-to'],
        user_id=3
    )
    db.session.add(insertDate)
    db.session.commit()

    resp = jsonify({'ok': 'ok'})
    resp.status_code = 200
    return resp