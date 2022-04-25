import sys,os
sys.path.append(os.getcwd())

from src.common.actions import Actions
from src.common.request import Request
from src.common.response import Response
from src.components.client.socket_client import SocketClient
from uuid import uuid4 as Uuid
from src.common.models.person import Person


def insert_person(connection, read_response):
    person = Person(
        id=Uuid(),
        name="Fulano",
        cpf="52646598656",
        address="Rua Xyz, 123"
    )

    request = Request(
        payload=person,
        action=Actions.CREATE,
        route="person"
    )

    connection.send(request.to_json())

    response = read_response(connection)
    print(response)

