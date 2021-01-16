from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import string
import random


app = Flask(__name__)
CORS(app)

users = {
    'users_list':
    [
        {
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job' : 'Janitor',
        },
        {
            'id' : 'abc123',
            'name' : 'Mac',
            'job' : 'Bouncer',
        },
        {
            'id' : 'ppp222',
            'name' : 'Bruno',
            'job' : 'Professor',
        },
        {
            'id' : 'yat999',
            'name' : 'Dee',
            'job' : 'Aspiring Actress',
        },
        {
            'id' : 'zap555',
            'name' : 'Dennis',
            'job' : 'Bartender',
        }
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        # Gets the value of any records matching 'name'
        search_username = request.args.get('name')
        # gets the value of any records matching 'job'
        search_job = request.args.get('job')

        if search_username or search_job:
            subdict = {'users_list' : []}

            for user in users['users_list']:
                if search_username and search_job:
                    if user['name'] == search_username and user['job'] == search_job:
                        subdict['users_list'].append(user)
                else: 
                    if user['name'] == search_username:
                        subdict['users_list'].append(user)
                    if user['job'] == search_job:
                        subdict['users_list'].append(user)

            return subdict

        return users
    
    elif request.method == 'POST':
        userToAdd = request.get_json()

        # Generates a random ID and adds the 'id' field to a user POST request (6.2)
        idToAdd = generate_id()
        userToAdd['id'] = idToAdd

        users['users_list'].append(userToAdd)

        # Updated representation of 'user' is sent to the frontend (6.3)
        resp = jsonify(user=userToAdd, success=True)

        # 201 = default code for a normal/OK POST
        # Code changed from 200 to 201 (6.1)
        resp.status_code = 201
        return resp

    elif request.method == 'DELETE':
        userToDelete = request.get_json()
        
        for user in users['users_list']:
            if user['id'] == userToDelete['id']:
                users['users_list'].remove(user)
                resp = jsonify(success=True)
                # 204 = default code for a normal/OK DELETE
                resp.status_code = 204
                return resp
        
        resp = jsonify(success=False)
        # 404 = when the user does not exist (Not Found)
        resp.status_code = 404
        return resp


# random ID generator function (6.2)
def generate_id():
    id = ""

    for i in range(3):
        id += random.choice(string.ascii_lowercase)

    for i in range(3):
        id += random.choice(string.digits)

    return id


@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})

    return users
