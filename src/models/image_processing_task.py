from enum import Enum
import uuid

# Define an enumeration for image processing operations
class ImageModification(Enum):
    EDGE_DETECTION = 1
    BLUR = 2
    ENHANCE_BRIGHTNESS = 3

# Represents a job that applies effects to an image
class ImageTask:
    def __init__(self, mod_type: ImageModification, img_src: str):
        self.task_id = str(uuid.uuid4()) # Generate a unique identifier
        self.mod_type = mod_type # Store the type of image modification
        self.img_src = img_src # Image source path
    
    def get_output_path(self):
        # Derive a path for saving processed images
        return "output_images/" + self.task_id + ".png"
