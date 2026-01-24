import assets
from Box import Box
from Conveyor import Conveyor

class Collector(Conveyor):
    def __init__(self, x, y, scale=0.1):
        self.base_img = assets.COLLECTOR_IMG.copy()
        super().__init__(x, y, 0, scale)

    def collisionHandler(self, box : Box):
        self.moveToCenter(box)
        if self.isBoxCentered(box):
            box.deleteBox()

    def moveToCenter(self, box : Box): # move the box to the center of the collector
        box_x, box_y = box.getMiddle()
        collector_x, collector_y = self.getMiddle()
        box.setPosition(collector_x - box.getSize()/2, collector_y - box.getSize()/2)