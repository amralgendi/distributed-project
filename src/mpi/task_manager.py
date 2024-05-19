import threading
from models.events import Event
from rmq.rmq_receiver import RMQEventReceiver
import subprocess

from rmq.rmq_sender import send_to_rmq

class MPITask(threading.Thread):
    def __init__(self, num_of_nodes, process_id, img_path, op_id):
        super().__init__()

        self.num_of_nodes = num_of_nodes
        self.process_id = process_id
        self.img_path = img_path
        self.op_id = op_id

    def run(self):
        result = subprocess.run(['mpiexec   ', '-n', str(self.num_of_nodes), 'python3', "-m", "mpi.worker", self.process_id, self.img_path, self.op_id]) 
        print(result)

        del self



class TaskManager():

    def __init__(self):
        super().__init__()
        self.zmqReceiver = RMQEventReceiver([Event.START_PROCESSING, Event.ADD_NODE, Event.REMOVE_NODE], self.didRecieveMessage)
        with open('/home/ubuntu/host_num', 'r') as file:
            current_value = file.read().strip()
        self.num_of_nodes = int(current_value) or 1
    
    def didRecieveMessage(self, event: Event, data: str):
        if event == Event.ADD_NODE:
            self.num_of_nodes += 1
            return
        if event == Event.REMOVE_NODE:
            self.num_of_nodes -= 1
            return
        if event == Event.START_PROCESSING:
            dataSplit = data.split(" ")
            print(dataSplit)
            process_id = dataSplit[0]
            img_path = dataSplit[1]
            op_id = dataSplit[2]

            data = " ".join([process_id, str(self.num_of_nodes)])
            send_to_rmq(Event.PROCESSING_STARTED, data)

            newThread = MPITask(self.num_of_nodes, process_id, img_path, op_id)
            newThread.start()
            return


    def startListening(self):
        self.zmqReceiver.start()


task_manager = TaskManager()

if __name__ == '__main__':
    task_manager.startListening()