"""flask_server.py - a simple Flask web server 

See https://flask.palletsprojects.com/en/2.2.x/quickstart/

Prerequisite: Make sure the fastapi package is installed. If not, use the command:
    pip install fastapi

To start the server, use the command:
    flask --app flask_server run

You can test it from the same machine in a browser using the loopback IP address (127.0.0.1)
and port (5000). So from a browser, try these URLs:
    http://127.0.0.1:5000               - returns a simple JSON dictionary
    http://127.0.0.1:5000/html          - returns a simple HTML page
    http://127.0.0.1:5000/rand/10/20    - returns a random integer between 10 and 20

If hosting on replit (which doesn't have a local browser), run main.py instead.
"""

from flask import Flask, request
from random import randint

app = Flask(__name__)

# An example of a simple web API returning JSON data (a Python dictionary)
# Called from http://127.0.0.1:5000
@app.route("/")
def get_root():
    return {"Hello": "World"}

# A simple response from a different path that returns HTML
# Called from http://127.0.0.1:5000/html
@app.route("/html")
def get_html():
    return "<html><body><h1>An HTML header</h1><p>And a paragraph</p></body></html>"

# A response to a request that takes user-defined input in the path
# Called from http://127.0.0.1:5000/rand/<min_value>/<max_value>
@app.route("/rand/<int:min>/<int:max>")
def get_rand(min, max):
    return str(randint(min, max))

