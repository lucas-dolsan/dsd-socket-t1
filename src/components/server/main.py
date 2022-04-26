import sys,os
sys.path.append(os.getcwd())

from src.common.response import Response
from src.components.server.request_router import RequestRouter
from src.common.request import Request
from src.common.connection import Connection
from parallel_socket_server import ParallelSocketServer

def on_connection_received_handler(connection: Connection):
    print('received client connection')
    request_router=RequestRouter()
    
    while True:
        request_json = connection.read()
        if not request_json:
            continue

        request = Request.from_json(request_json)

        response = request_router.handle_request(request)

        connection.send(response.to_json())

        connection.close()

server = ParallelSocketServer()
server.listen(on_connection_received_handler)
