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

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        # Gets the value of any records matching 'name'
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        # 200 = default code for a normal/OK response
        resp.status_code = 200
        return resp

@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})

    return users
