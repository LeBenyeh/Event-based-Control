from enum import Enum

class SectionType(Enum):
    CONVEYOR_START = "ConveyorStart"
    CONVEYOR_MID = "ConveyorMid"
    CONVEYOR_TOP = "ConveyorEnd"
    CONVEYOR_BOT = "ConveyorBottom"
    CORNER = "Corner"
    SELECTOR = "Selector"
    CONVEYOR = "Conveyor"