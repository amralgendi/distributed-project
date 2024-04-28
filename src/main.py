

import cv2
from models.image_processing_task import ImageModification, ImageTask
from worker import WorkerThread


if __name__ == "__main__":
    src_path = "./uploaded_imgs/img.jpeg"
    new_task = ImageTask(ImageModification.ENHANCE_BRIGHTNESS, src_path)

    worker_thread = WorkerThread(new_task)
    worker_thread.start()