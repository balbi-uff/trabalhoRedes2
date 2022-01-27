import socket
import random
import time
import requests
import json
import os

#os.chdir("trabalhoRedes2")


def socket_way():
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = bytes("lixo".encode())


    

    ip = "142.251.132.78"
    port = 8080
    duration = 2
    timeout = time.time() + duration
    sent = 0

    while True:
        if time.time() > timeout:
            break
        socket_.sendto(data, (ip, port))
        sent += 1
        print(f"Packet {sent} sent")


def request_way():
    ip = "http://localhost"
    port = "8000"
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