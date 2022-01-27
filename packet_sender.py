import socket
import random
import time
import requests

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
    ip = "192.168.0.110"
    port = 8080
    n_of_requests = 10

