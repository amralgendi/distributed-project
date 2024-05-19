from enum import Enum
import uuid
from constants import PROCESSED_PATH

# Define an enumeration for image processing operations
class ImageModification(Enum):
    EDGE_DETECTION = 1
    BLUR = 2
    ENHANCE_BRIGHTNESS = 3

# Represents a job that applies effects to an image
class ImageTask:
    def __init__(self, id: str, img_path: str, mod_type: ImageModification):
        self.task_id = id # Generate a unique identifier
        self.mod_type = mod_type # Store the type of image modification
        self.img_path = img_path
    
    def get_output_path(self):
        # Derive a path for saving processed images
        return PROCESSED_PATH + self.id + ".png"