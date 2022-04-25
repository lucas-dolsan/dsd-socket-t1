import sys,os

sys.path.append(os.getcwd())

from src.common.actions import Actions
from src.common.request import Request
from src.common.response import Response
from src.components.client.socket_client import SocketClient
from uuid import uuid4 as Uuid
from src.common.models.person import Person

client = SocketClient()
connection = client.connect()

if not connection:
    raise Exception("unable to connect")

person = Person(
  id=Uuid(),
  name="Fulano",
  cpf="52646598656",
  address="Rua Xyz, 123"
)

request = Request(payload=person, action=Actions.CREATE, route="person")

connection.send(request.to_json())

while True:
    response_json = connection.read()
    if not response_json:
        continue

    response = Response.from_json(response_json)

    print(response)
