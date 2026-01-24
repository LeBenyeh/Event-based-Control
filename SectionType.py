from enum import Enum

class SectionType(Enum):
    CONVEYOR_START = "ConveyorStart"
    CONVEYOR_MID1 = "ConveyorMid"
    CONVEYOR_MID2 = "ConveyorMid2"
    CONVEYOR_TOP1 = "ConveyorTop"
    CONVEYOR_TOP2 = "ConveyorTop2"
    CONVEYOR_TOP3 = "ConveyorTop3"
    CONVEYOR_TOP4 = "ConveyorTop4"
    CONVEYOR_BOT1 = "ConveyorBottom"
    CONVEYOR_BOT2 = "ConveyorBottom2"
    CONVEYOR_BOT3 = "ConveyorBottom3"
    CONVEYOR_BOT4 = "ConveyorBottom4"
    CORNER = "Corner"
    SELECTOR = "Selector"
    CONVEYOR = "Conveyor"
    TRANSFORMER = "Transformer"