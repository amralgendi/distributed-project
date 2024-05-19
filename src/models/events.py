
from enum import Enum


class Event(Enum):
    NODE_FAILED = 1
    PROCESSING_FAILED = 2
    PROCESSING_DONE = 3
    PROGRESS_UPDATE = 4
    START_PROCESSING = 5
    NODE_DONE = 6
    PROCESSING_STARTED = 7
    ADD_NODE = 8
    REMOVE_NODE = 9