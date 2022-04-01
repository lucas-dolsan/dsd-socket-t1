import json

from src.common.message import Message

DEFAULT_BUFFER_SIZE=4096

class Connection:
    def __init__(self, socket_connection, address, port):
        self.socket_connection = socket_connection
        self.address = address
        self.port = port

        print(f'Host {address}:{str(port)} connected')

    def read(self):
        data = self.socket_connection.recv(DEFAULT_BUFFER_SIZE)
        return data

    def send_json(self, json_message: str):
        data = bytes(json_message, encoding="utf-8")
        self.socket_connection.send(data)

    def read_json(self):
        data = self.read()
        if data:
            return json.loads(data)

    def send_message(self, message: Message):
            self.send_json(message.to_json())

    def read_message(self) -> Message:
        json_message = self.read()
        return Message.from_json(json_message)
            
    def close(self):
        self.socket_connection.close()
