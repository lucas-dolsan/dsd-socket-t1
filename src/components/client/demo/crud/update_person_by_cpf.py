import sys,os
sys.path.append(os.getcwd())

from src.common.models.person import Person
from src.common.person_actions import PersonActions
from src.common.request import Request
from src.common.response import Response
from src.components.client.socket_client import SocketClient
from uuid import UUID, uuid4 as Uuid

def update_person_by_cpf(connection, read_response):
    updated_person = Person(
        id=Uuid(),
        name="Beltrano",
        cpf="52646598656",
        address="Rua Xpto, 321"
    )

    request=Request(
      payload=updated_person,
      action=PersonActions.UPDATE_BY_CPF,
      route="person"
    )

    connection.send(request.to_json())

    response = read_response(connection)
    print(response)
