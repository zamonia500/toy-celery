import os
from flask import Flask, url_for, redirect
from flask_pymongo import PyMongo
from mantra.webserver.apis.flasks import blueprint as api1_0

app = Flask(__name__)
# read config from webserver_config.json - config for dev only
app.config.from_json(os.path.abspath('webserver_config.json'))
# register all blueprints for versioning APIS
app.register_blueprint(api1_0)
# pymongo
mongo = PyMongo(app, app.config['DATABASE_URL'])

@app.route('/')
def default_swagger():
    return redirect(url_for('api1.0.doc'))

app.run(debug=True, port=app.config['PORT'])


