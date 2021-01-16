# Linking Frontend with Backend
## Developer: Steven Ngo

Make sure to have Flask installed, following the installation guide from here if need:
- https://flask.palletsprojects.com/en/1.1.x/installation/

Create and activate a virtual environment in the same folder as the repo files with the following:
```
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
  (if it is your first time using Flask)
```

In your virtual environment/venv, run the following:
```
set FLASK_APP=first_backend.py
set FLASK_ENV=development
```

To launch the backend:
```
flask run
(or alternatively, the below command works too)
python -m flask run
```

To launch the frontend:
```
npm start
```
