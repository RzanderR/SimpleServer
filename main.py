"""main.py - client to call one of the servers programatically
"""

import requests

SERVER = "127.0.0.1"  # Loopback - must start one of the servers first
PORT = 5000           # 5000 for Flask, 8000 for FastAPI
paths = ["", "/html", "/rand/10/20"]

BASE_URL = "http://" + SERVER + ":" + str(PORT)

def call_server(path : str = "") -> str:
  response = requests.get(BASE_URL + path)
  response.raise_for_status()
  return response.text

for path in paths:
  print ("Calling", BASE_URL + path)
  text = call_server(path)
  print (text)
  print()

