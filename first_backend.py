from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

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
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        # 200 = default code for a normal/OK POST
        resp.status_code = 200
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

@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})

    return users
