import sys,os
sys.path.append(os.getcwd())

from src.common.response import Response
from src.components.server.repositories.person_repository import PersonRepository
from src.components.server.request_router import RequestRouter
from src.common.request import Request
from src.common.connection import Connection
from parallel_socket_server import ParallelSocketServer

def on_connection_received_handler(connection: Connection):
        request_router=RequestRouter()
        
        while True:
            request_json = connection.read()
            if not request_json:
                continue

            request = Request.from_json(request_json)

            request_router.route_to_controller(request)

            response=Response(
                payload=201,
                request_id=request.id,
            )

            connection.send(response.to_json())

            connection.close()

server = ParallelSocketServer()
server.listen(on_connection_received_handler)

# TODO
#  - choose a extended theme in moodle
#  - properly close the connection on exit (BadFileDescriptor)
#  - generalize Message
#  - add an Id to Message
#  - create a Request extending Message
#  - create a Response extending Message
#  - reference the Request's id in the Response
#  - create an ActionMapper/ActionRouter that maps/routes Actions to an ActionHandler
#  - create a StorageAdapter interface
#  - create A MemoryStorageAdapter implementing StorageAdapter
#  - consider creating a MongoDbStorageAdapter
#  - consider modelling the ActionHandlers as Observers (while true)
#  - setup pipenv
#  - figure out a way to create .exe/.sh files, or something of the sort
#  - create a CLI to perform actions
#  - create unit tests
#  - create integration tests
#  - consider creating .puml docs
#  - create slideshow