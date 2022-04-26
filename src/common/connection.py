from dataclasses import dataclass
from socket import SHUT_RD, socket

from src.common.socket_message_encoder import SocketMessageEncoder

DEFAULT_BUFFER_SIZE=4096
DEFAULT_ENCODING='utf-8'
DEBUG=False

@dataclass
class Connection:
    socket_connection: socket
    address: str
    port: int
    message_encoder=SocketMessageEncoder(encoding=DEFAULT_ENCODING)

    def read(self) -> str:
        data = self.socket_connection.recv(DEFAULT_BUFFER_SIZE)
        decoded_data = self.message_encoder.decode(data)
        if DEBUG:
            print(f'Receiving data: {decoded_data}')
        return decoded_data

    def send(self, data: str):
        encoded_data=self.message_encoder.encode(data)
        if DEBUG:
            print(f'Sending data: {data}')
        self.socket_connection.send(encoded_data)

    def is_open(self):
        return not self.socket_connection._closed

    def close(self):
        self.socket_connection.close()