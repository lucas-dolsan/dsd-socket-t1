import sys,os
sys.path.append(os.getcwd())

from src.common.response import Response
from uuid import uuid4 as Uuid
from src.common.request import Request
from src.common.actions import Actions
from src.components.client.socket_client import SocketClient
from src.common.models.person import Person

    # return Person(
    #     id=Uuid(),
    #     name=name,
    #     cpf=cpf,
    #     address=address
    # )

from enum import Enum, unique

class OperationController:
    def read_operation(self):
        print('[C]REATE')
        print('[R]EAD')
        print('[U]PDATE')
        print('[D]ELETE')

        valid_op_list=['c', 'r', 'u', 'd']

        op=None

        while op not in valid_op_list:
            op=input('Operation: ')
            
            op=str.lower(op)

            if op not in valid_op_list:
                print('Invalid operation, try again...')
                continue

        self.handle_operation(op)

    def __init__(self):
        client = SocketClient()
        connection = client.connect()

        if not connection:
            raise Exception("unable to connect")

        self.connection=connection
        print('connected to server')

    def read_response(self):
        responded=False

        while not responded:
            response_json = self.connection.read()
            if not response_json:
                continue

            response = Response.from_json(response_json)
            responded=True

        return response

    def send_request(self, request: Request):
        self.connection.send(request.to_json())
        response = self.read_response()

        print(response)

    def handle_operation(self, operation):
        action=Actions.from_operation(operation)

        action_map={
            Actions.CREATE: self.create,
            Actions.READ: self.read,
            Actions.UPDATE: self.update,
            Actions.DELETE: self.delete,
        }

        action_map[action]()

    def create(self):
        print(' -- CREATE --')
        cpf = input('cpf: ')
        name = input('name: ')
        address = input('address: ')

        person = Person(
            id=Uuid(),
            name=name,
            cpf=cpf,
            address=address
        )

        request = Request(
            payload=person,
            action=Actions.CREATE,
            route="person"
        )

        self.send_request(request)


    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


controller = OperationController()

controller.read_operation()