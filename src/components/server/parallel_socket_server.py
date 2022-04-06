from socket import socket, error as SocketError
from _thread import start_new_thread
from src.common.connection import Connection
from src.components.server.config import ADDRESS, PORT

class ParallelSocketServer:
    def __init__(self):
        self.socket = socket()

    def _handle_connection(self, connection, host, on_message_callback):
        address, port = host
        connection = Connection(connection, address, port)

        start_new_thread(on_message_callback, (connection, ))
        
    def listen(self, on_connection_handler):
        try:
            self.socket.bind((ADDRESS, PORT))
        except SocketError as err:
            print(str(err))

        print(f'Listening on {ADDRESS}:{PORT}...')

        self.socket.listen()

        while True:
            connection, host = self.socket.accept()
            self._handle_connection(connection, host, on_connection_handler)
