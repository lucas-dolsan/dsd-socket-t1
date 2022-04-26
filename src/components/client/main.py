import sys,os
sys.path.append(os.getcwd())

from src.components.client.operation_controller import OperationController

def main():
    controller = OperationController()

    exit=False

    while not exit:
        controller.read_operation()
        print("----------------------------------------------")
        answer=input("Type 'exit' to stop, or hit enter to run another operation \n")
        if answer == "exit":
            exit=True

    controller.close()

main()