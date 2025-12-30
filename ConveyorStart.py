from Conveyor import Conveyor

class ConveyorStart(Conveyor):
    def __init__(self, conveyor):
        # remove old conveyor to avoid duplication
        try:
            Conveyor.conveyorsList.remove(conveyor)
        except ValueError:
            pass
        super().__init__(conveyor.rect.x, conveyor.rect.y, angle=conveyor.angle)