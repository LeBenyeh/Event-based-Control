import pygame
import assets
from Box import Box
from settings import BOX_SPEED
from SectionType import SectionType

class Conveyor:
    conveyorsList = []
    def __init__(self, x, y, angle=0, scale=0.1):
        if hasattr(self, 'base_img'):
            img = self.base_img
        else:
            img = assets.CONVEYOR_IMG.copy()

        w, h = img.get_size()
        new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))
        self.base_img = pygame.transform.scale(img, (new_w, new_h))
        self.surface_color = pygame.transform.rotate(self.base_img, angle)
        self.surface_gray = pygame.transform.grayscale(self.surface_color.copy())
        self.surface = self.surface_gray
        self.rect = self.surface.get_rect(topleft=(x, y))
        self.angle = angle
        self.state = 0
        self.section = SectionType.CONVEYOR
        Conveyor.conveyorsList.append(self)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def activate(self):
        self.state = 1
        self.surface = self.surface_color

    def stop(self):
        self.state = 0
        self.surface = self.surface_gray

    def getMiddle(self):
        return self.rect.center
    
    def getSize(self):
        return self.rect.size

    def getAngle(self):
        return self.angle
    
    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        center = self.rect.center
        self.surface_color = pygame.transform.rotate(self.base_img, self.angle)
        self.surface_gray = pygame.transform.grayscale(self.surface_color.copy())
        self.surface = self.surface_color if self.state == 1 else self.surface_gray
        self.rect = self.surface.get_rect(center=center)

    def collisionHandler(self, box : Box):
        self.moveToFacingDirection(box)

    def moveBox(self, box :Box, dir : str):
        match dir:
            case 'up':
                box.setSpeed(0, -BOX_SPEED)
            case 'down':
                box.setSpeed(0, BOX_SPEED)
            case 'left':
                box.setSpeed(-BOX_SPEED, 0)
            case 'right':
                box.setSpeed(BOX_SPEED, 0)
    
    def moveToFacingDirection(self, box: Box):

        angle = self.getAngle()
        if angle == 0:
            self.moveBox(box, 'up')
        elif angle in (180, -180):
            self.moveBox(box, 'down')
        elif angle in (-90, 270):
            self.moveBox(box, 'right')
        elif angle in (90, -270):
            self.moveBox(box, 'left')

    def moveToCenter(self, box: Box):
        sx, sy = self.getMiddle()
        bx, by = box.getMiddle()
        angle = self.getAngle()

        if angle == 0 and by < sy:
            self.moveBox(box, 'down')
        elif angle in (180, -180) and by > sy:
            self.moveBox(box, 'up')
        elif angle in (-90, 270) and bx > sx:
            self.moveBox(box, 'left')
        elif angle in (90, -270) and bx < sx:
            self.moveBox(box, 'right')
    
    def isBoxCentered(self, box, tol: int = 3) -> bool:
        """Return True if the center of `box` is within `tol` pixels of this conveyor's center.

        Uses Euclidean distance between centers.
        """
        bx, by = box.getMiddle()
        cx, cy = self.getMiddle()
        import math
        return math.hypot(bx - cx, by - cy) <= tol
    
    def getSection(self):
        return self.section
    
    def setSection(self, section_str):
        self.section = section_str

    def showEdges(self, screen):
        pygame.draw.rect(screen, (0,0,255), self.rect, 5)