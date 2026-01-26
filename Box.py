import pygame
from settings import RED, BLUE, GREEN, BLACK
import assets

class Box:
    boxList = []
    def __init__(self, x=0, y=0, xspeed=0, yspeed=0, size=20, color=RED):
        
        box_img = assets.BOX_IMG.copy()
        box_img = pygame.transform.scale(box_img, (size, size))
        self.color = color
        if color == RED:
            box_img.fill(RED, special_flags=pygame.BLEND_RGBA_MULT)
        elif color == BLUE:
            box_img.fill(BLUE, special_flags=pygame.BLEND_RGBA_MULT)
        elif color == GREEN:
            box_img.fill(GREEN, special_flags=pygame.BLEND_RGBA_MULT)
        elif color == BLACK:
            box_img.fill(BLACK, special_flags=pygame.BLEND_RGBA_MULT)
        self.size = size
        self.surface = box_img
        self.rect = self.surface.get_rect(topleft=(x, y))
        self.pos = pygame.Vector2(x, y)
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.boxList.append(self)

    def update(self, dt):
        self.pos.x += self.xspeed * dt
        self.pos.y += self.yspeed * dt

        self.rect.topleft = self.pos

    def draw(self, target_surface):
        target_surface.blit(self.surface, self.rect)

    def collision(self, conveyor) -> bool:
        return self.rect.colliderect(conveyor.rect)

    def collisionBox(self, otherBox: Box) -> bool:
        return self.rect.colliderect(otherBox.rect)
    
    def getMiddle(self):
        return self.rect.center
    
    def setSpeed(self, xspeed, yspeed):
        self.xspeed = xspeed
        self.yspeed = yspeed

    def getSpeed(self):
        return (self.xspeed, self.yspeed)
    
    def getPosition(self):
        return (self.pos.x, self.pos.y)
    
    def setPosition(self, x, y):
        self.pos.x = x
        self.pos.y = y
    
    def getSize(self):
        return self.size

    def getColor(self):
        return self.color
    
    def deleteBox(self): # delete the box from the list of boxes
        self.boxList.remove(self)