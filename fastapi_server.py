"""Server.py - a FastAPI web server

This is a simple web server using code from https://fastapi.tiangolo.com/#create-it

To run it, use the command:
uvicorn fastapi_server:app --reload

You can test it from the same machine using the loopback IP address 127.0.0.1 and port 8000
So from a browser, try these URLs:
http://127.0.0.1:8000    - should return a JSON dictionary hello world
http://127.0.0.1:8000/html - should return a simple HTML page
http://127.0.0.1:8000/randint/10/20 - should return a random integer between 10 and 20
"""

from random import randint
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Start the fastapi server
app = FastAPI()

# Respond to root URL requests (http://server) with a simple dictionary
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Respond to the html path (http://server/html) with some simple HTML
@app.get("/html", response_class=HTMLResponse)
def read_html():
    html_text = "<html><body><h1>An HTML header</h1><p>And a paragraph</p></body></html>"
    return HTMLResponse(content=html_text, status_code=200)

# Respond to the randint URL requests with min and max values with a random int
# http://server/randint/{min_val}/{max_val}
@app.get("/rand/{min}/{max}")
def read_rand(min : int, max : int):
    #return str(randint(min, max))
    return randint(min, max)
