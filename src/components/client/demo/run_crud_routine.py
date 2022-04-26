import sys,os
sys.path.append(os.getcwd())

from src.components.client.demo.crud.insert_person import insert_person
from src.components.client.demo.crud.read_person_by_cpf import read_person_by_cpf
from src.components.client.demo.crud.update_person_by_cpf import update_person_by_cpf
from src.components.client.demo.crud.delete_person_by_cpf import delete_person_by_cpf

from src.common.response import Response
from src.components.client.socket_client import SocketClient

def setup_connection():
    client = SocketClient()
    connection = client.connect()

    if not connection:
        raise Exception("unable to connect")
    return connection

def read_response(connection):
    responded=False

    while not responded:
        response_json = connection.read()
        if not response_json:
            continue

        response = Response.from_json(response_json)
        responded=True

    return response

def main():
    connection=setup_connection()

    insert_person(connection, read_response)
    read_person_by_cpf(connection, read_response)
    update_person_by_cpf(connection, read_response)
    delete_person_by_cpf(connection, read_response)
    read_person_by_cpf(connection, read_response)

main()