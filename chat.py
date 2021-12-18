# IMPORTS
import os
import socket
from dotenv import load_dotenv

load_dotenv()

# CONSTANTS

server = os.environ.get('SERVER')
port = int(os.environ.get('PORT'))
nickname = os.environ.get('NICKNAME')
token = os.environ.get('TOKEN')
channel = os.environ.get('CHANNEL')

# START OF SCRIPT

socket = socket.socket()
socket.connect((server, port))

socket.send(f"PASS {token}\n".encode('utf-8'))
socket.send(f"NICK {nickname}\n".encode('utf-8'))
socket.send(f"JOIN {channel}\n".encode('utf-8'))


while True:
    response = socket.recv(2048).decode('utf-8')
    print(response)
