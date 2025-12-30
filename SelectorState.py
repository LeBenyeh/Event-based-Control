from enum import Enum

class SelectorState(Enum):
    IDLE = 0
    RECEIVING = 1
    ROTATING = 2
    SENDING = 3
    RESETTING = 4
