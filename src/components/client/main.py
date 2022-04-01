import sys,os
sys.path.append(os.getcwd())

from src.common.actions import Actions
from src.common.message import Message
from src.components.client.socket_client import SocketClient
from src.common.models.person import Person

def get_person_from_stdin() -> Person:
    name = input('person name: ')
    cpf = input('person cpf: ')
    address = input('person address: ')

    return Person(
        name=name,
        cpf=cpf,
        address=address
    )

client = SocketClient()
connection = client.connect()

if not connection:
    raise Exception("unable to connect")

person = get_person_from_stdin()
message = Message(Actions.CREATE, person)

print(f'sending message: {message}')

connection.send_message(message)

