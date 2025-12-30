import pygame
from Conveyor import Conveyor
import assets
from settings import BOX_SPEED
from SectionType import SectionType

class Corner(Conveyor):
    cornerList = []
    def __init__(self, x, y, angle=0, scale=0.1, flip=False):
        self.base_img = assets.CORNER_IMG.copy()  
        if flip:
            self.base_img = pygame.transform.flip(self.base_img, True, False)
        
        super().__init__(x, y, angle, scale)
        self.flip = flip
        self.section = SectionType.CORNER
        self.cornerList.append(self)

    def getFlip(self):
        return self.flip

    def collisionHandler(self, box):

        bx, by = box.getMiddle()
        cx, cy = self.getMiddle()
        flip = -1 if self.flip else 1

        if self.angle == 0:
            if by < cy:
                box.setSpeed(BOX_SPEED * flip, 0)
            else:
                box.setSpeed(0, -BOX_SPEED)

        elif self.angle in (-90, 270):
            if bx > cx:
                box.setSpeed(0, BOX_SPEED * flip)
            else:
                box.setSpeed(BOX_SPEED, 0)

        elif self.angle in (180, -180):
            if by > cy:
                box.setSpeed(-BOX_SPEED * flip, 0)
            else:
                box.setSpeed(0, BOX_SPEED)

        elif self.angle in (90, -270):
            if bx < cx:
                box.setSpeed(0, -BOX_SPEED * flip)
            else:
                box.setSpeed(-BOX_SPEED, 0)
