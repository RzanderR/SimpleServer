"""flask_server.py - a simple web server using Flask

See https://flask.palletsprojects.com/en/2.2.x/quickstart/

Prerequisite: Make sure the fastapi package is installed. If not, use the command:
    pip install fastapi

To start the server, use the command:
    flask --app flask_server run

You can test it from the same machine in a browser using the loopback IP address (127.0.0.1)
and port (5000). So from a browser, try these URLs:
    http://127.0.0.1:5000               - returns a simple HTML page
    http://127.0.0.1:5000/rand/10/20    - returns a random integer between 10 and 20
"""

from flask import Flask, request
from random import randint

app = Flask(__name__)

# An example of a simple response
@app.route("/")
def get_root():
    return "<h1>An important message</h1><p>Hello, World!</p>"

# An example of a response that takes parameters in the path
@app.route("/rand/<int:min>/<int:max>")
def get_rand(min, max):
    return str(randint(min, max))

