from enum import Enum

class SectionType(Enum):
    CONVEYOR_START = "ConveyorStart"
    CONVEYOR_MID = "ConveyorMid"
    CONVEYOR_MID2 = "ConveyorMid2"
    CONVEYOR_TOP = "ConveyorTop"
    CONVEYOR_TOP2 = "ConveyorTop2"
    CONVEYOR_BOT = "ConveyorBottom"
    CONVEYOR_BOT2 = "ConveyorBottom2"
    CORNER = "Corner"
    SELECTOR = "Selector"
    CONVEYOR = "Conveyor"
    TRANSFORMER = "Transformer"