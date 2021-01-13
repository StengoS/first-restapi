from flask import Flask
from flask import request


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

@app.route('/users')
def get_users():
    # Gets the value of any records matching 'name'
    search_username = request.args.get('name')
    if search_username:
        subdict = {'users_list' : []}
        for user in users['users_list']:
            if user['name'] == search_username:
                subdict['users_list'].append(user)
        return subdict

    return users
