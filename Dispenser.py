import random
import assets
import time
from Conveyor import Conveyor
from Box import Box
from settings import BLUE,RED,GREEN,DISPENSER_COOLDOWN

class Dispenser(Conveyor):
    def __init__(self, x, y, angle=0, scale=0.1):
        self.base_img = assets.DISPENSER_IMG.copy()
        super().__init__(x, y, angle, scale)
        self.last_dispense_time = 0
        self.cooldown_seconds = DISPENSER_COOLDOWN
    def dispense(self):
        
        current_time = time.time()
        if current_time - self.last_dispense_time < self.cooldown_seconds:
            print(f"Cooldown: {self.cooldown_seconds - (current_time - self.last_dispense_time)} seconds remaining")
        else :
            self.last_dispense_time = current_time
            disp_x, disp_y = self.getMiddle()
            random_color = random.choice((RED, BLUE, GREEN))
            box = Box(color=random_color)
            box_size = box.getSize()
            box.setPosition(disp_x - box_size/2, disp_y - box_size/2)


