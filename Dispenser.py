import assets
from Conveyor import Conveyor

class Dispenser(Conveyor):
    def __init__(self, x, y, angle=0, scale=0.1):
        self.base_img = assets.DISPENSER_IMG.copy()
        super().__init__(x, y, angle, scale)
    def dispense(self):
        print("Dispensing...")
