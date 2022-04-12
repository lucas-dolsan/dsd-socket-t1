import sys,os
sys.path.append(os.getcwd())

from src.common.response import Response
from uuid import uuid4 as Uuid
from src.common.request import Request
from src.common.actions import Actions
from src.components.client.socket_client import SocketClient
from src.common.models.person import Person

def get_person_from_stdin() -> Person:
    name = input('person name: ')
    cpf = input('person cpf: ')
    address = input('person address: ')

    return Person(
        id=Uuid(),
        name=name,
        cpf=cpf,
        address=address
    )

client = SocketClient()
connection = client.connect()

if not connection:
    raise Exception("unable to connect")

person = get_person_from_stdin()
request = Request(payload=person, action=Actions.CREATE, route="person")

connection.send(request.to_json())

while True:
    response_json = connection.read()
    if not response_json:
        continue

    response = Response.from_json(response_json)

    print(response)



