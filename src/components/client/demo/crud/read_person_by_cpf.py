import sys,os
sys.path.append(os.getcwd())

from src.common.models.person import Person
from src.common.person_actions import PersonActions
from src.common.request import Request

def read_person_by_cpf(connection, read_response):
    request=Request(
      payload={ "cpf": "52646598656" },
      action=PersonActions.READ_BY_CPF,
      route="person"
    )

    connection.send(request.to_json())

    response = read_response(connection)
    print(response)


