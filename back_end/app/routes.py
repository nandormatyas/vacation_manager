from app import app, db, jwt
import requests
import os
import json
from . import models
from flask import jsonify, render_template, request, redirect, make_response
from flask_cors import CORS
from google_config import flow_config
from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, get_jwt_claims
)

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


# @app.route('/google_auth')
# def google_auth():

    # return render_template('index.html', title="Calendar")

    # resp = make_response(redirect('/index'))
    # resp.set_cookie('username', username)
    # return resp


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'user': identity
    }
@app.route('/index')
def index():
    # try:
        credentials = flow.step2_exchange(request.args.get('code'))
        userData = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=' + credentials.access_token).content
        userData = json.loads(userData.decode('utf-8'))
        existing_user = models.User.query.filter(models.User.email == userData['email']).first()
        if existing_user:
            user = {
                'user_id': existing_user.id,
                'user_role': existing_user.role,
                'user_email': existing_user.email,
                'user_name': existing_user.name
            }
            resp = make_response(render_template('index.html', title="Calendar", user=user))
            resp.set_cookie(create_access_token(identity=user))
            return resp
        else:
            user = {
                'name': userData['name'],
                'email': userData['email'],
                'googleId': userData['id']
            }
            insertUser = models.User(**user)
            db.session.add(insertUser)
            db.session.commit()
            return redirect('/index')
    # except:
    #     return render_template('login.html')


@app.route('/calendar')
@jwt_required
def calendar():

    print(request.headers.get('Authorization'))
    claims = get_jwt_claims()
    print(claims)

    events = models.Vacation.query.all()
    eventList = []
    for event in events:
        vacation_approval_status = {
            0: 'pending',
            1: 'approved',
            2: 'denied'
        }
        eventObject = {
            'title': str(event.user_id) + ' Vacation ' + vacation_approval_status[event.status],
            'start': event.fromDate,
            'end': event.toDate
        }
        eventList.append(eventObject)
    resp = jsonify(eventList)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return resp

@app.route('/vacation_request', methods=['POST'])
def vacation_request():
    insertDate = models.Vacation(
        fromDate=request.form['date-from'],
        toDate=request.form['date-to'],
        user_id=request.form['user']
    )
    db.session.add(insertDate)
    db.session.commit()

    resp = jsonify({'ok': 'ok'})
    return resp
    # return redirect('/index')
