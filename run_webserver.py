from flask import Flask, url_for, redirect
from webserver.apis.flasks import blueprint as api1_0

app = Flask(__name__)
app.register_blueprint(api1_0)

@app.route('/')
def default_swagger():
    return redirect(url_for('api1.0.doc'))

app.run(debug=True)


