import cv2
import numpy as np
from mpi4py import MPI
import threading
import os

from models.image_processing_task import ImageTask
from processing import modify_image, split_image

class WorkerThread(threading.Thread):
    def __init__(self, task: ImageTask):
        super().__init__()
        self.task = task

    def run(self):
        if(not os.path.isdir("output_images")):
            os.mkdir("output_images")

        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        size = comm.Get_size()

        if rank == 0:
            image_data = split_image(self.task.img_src, size)
        else:
            image_data = None

        local_chunk = comm.scatter(image_data, root=0)

        filtered_chunk = modify_image(self.task.mod_type, local_chunk)

        all_filtered_chunks = comm.gather(filtered_chunk, root=0)

        if rank == 0:
            filtered_image = np.concatenate(all_filtered_chunks, axis=1)
            cv2.imwrite(self.task.get_output_path(), filtered_image) 
