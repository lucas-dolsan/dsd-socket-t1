
from src.common.connection import Connection
from socket import socket, error as SocketError
from src.components.server.config import ADDRESS, PORT

class SocketClient:
    def __init__(self):
        self.socket = socket()
    def connect(self) -> Connection:
        try:
            connection = Connection(self.socket, ADDRESS, PORT)
            self.socket.connect((ADDRESS, PORT))
            return connection
        except SocketError as err:
            print(str(err))
