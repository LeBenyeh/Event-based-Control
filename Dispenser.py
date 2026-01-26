import random
import assets
from Conveyor import Conveyor
from Box import Box
from settings import BLUE,RED,GREEN, BLACK

class Dispenser(Conveyor):
    def __init__(self, x, y, angle=0, scale=0.1):
        self.base_img = assets.DISPENSER_IMG.copy()
        super().__init__(x, y, angle, scale)
    def dispense(self):
        if self.collisionWithBox():
            print("Cannot dispense a box : a box is on the dispenser")
        else:
            disp_x, disp_y = self.getMiddle()
            random_color = random.choice((RED, BLUE, GREEN, BLACK))
            box = Box(color=random_color)
            box_size = box.getSize()
            box.setPosition(disp_x - box_size/2, disp_y - box_size/2)

    def collisionWithBox(self):
        for b in Box.boxList:
            if self.rect.colliderect(b.rect):
                return True
        return False


