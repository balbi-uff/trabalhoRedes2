import socket
import random
import time
import requests
import json
import os

def request_way():
    ip = "http://192.168.0.109" # IP of the server
    port = "8000"               # Port of the server
    n_of_requests = 10
    json_filename = "message.json"
    responses = {}
    
    with open(json_filename) as json_file:
        json_data = json_file.read()
        parsed_json = (json.loads(json_data))

    for i in range(n_of_requests):
        data = requests.post(
                        url=ip + ":" + port,
                        data=json.dumps(parsed_json),
                        headers={"Content-Type": "application/json"}
        )
        responses[i] = data.text
        print(f"Request {i} sent, response was:\n{responses[i]}\nEOR\n")


try:
    request_way()
except requests.exceptions.InvalidSchema as e:
    print("SERVER WAS NOT FOUND!")
    print(f"Error: {e}")