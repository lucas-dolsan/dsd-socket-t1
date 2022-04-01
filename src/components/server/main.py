import sys,os
sys.path.append(os.getcwd())

from src.common.connection import Connection
from src.common.models.person import Person
from parallel_socket_server import ParallelSocketServer

people=[]

print(f'before: people={people}')

def on_connection_received_handler(connection: Connection):
        while True:
            message = connection.read_message()

            if not message:
                continue

            person = Person.from_json(message.payload)

            people.append(person)

            print(f'after: people={people}')
            
            connection.close()

server = ParallelSocketServer()
server.listen(on_connection_received_handler)

# TODO
#  - choose a extended theme in moodle
#  - properly close the connection on exit
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