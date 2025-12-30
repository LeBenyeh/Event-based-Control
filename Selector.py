from unittest import case
import assets
import pygame
from SelectorState import SelectorState
from Conveyor import Conveyor
from Box import Box
from DetectionZone import DetectionZone
from settings import RED, GREEN, BLUE
from SectionType import SectionType

class Selector(Conveyor):
    RADIUS = 50  # Define a radius for detecting nearby conveyors
    DETECT_MARGIN = 1  # Margin for exit zone detection
    selectorList = []
    def __init__(self, x=0, y=0, angle=0,scale=0.1, entryZone: str='up'):
        self.base_img = assets.SELECTOR_IMG.copy()
        super().__init__(x, y, angle, scale)
        self.state_machine = SelectorState.IDLE
        self.detectionZone = DetectionZone(self)
        self.setEntryZone(self.rect, entryZone)
        self.resetExitZone()
        self.collision = False
        self.currentBoxColor = None
        self.section = SectionType.SELECTOR
        self.selectorList.append(self)
    
    def collisionHandler(self, box):
        self.collision = True

    def stateHandler(self, box):
        #print(f"State machine: {self.state_machine}")
        match self.state_machine:
            case SelectorState.IDLE:
                self.activateFrontConveyorSection()

            case SelectorState.RECEIVING:
                self.moveToCenter(box)
                if self.collision:
                    self.stopFrontConveyorSection()
                if self.isBoxCentered(box): self.state_machine = SelectorState.ROTATING
                
            case SelectorState.ROTATING:
                if self.currentBoxColor == RED:
                    self.rotate(-90)
                elif self.currentBoxColor == BLUE:
                    self.rotate(180)
                elif self.currentBoxColor == GREEN:
                  self.rotate(90)
                self.state_machine = SelectorState.SENDING
            case SelectorState.SENDING:
                self.moveToFacingDirection(box)
            
            case SelectorState.RESETTING:
                if self.currentBoxColor == RED:
                    self.rotate(90)
                elif self.currentBoxColor == BLUE:
                    self.rotate(-180)
                elif self.currentBoxColor == GREEN:
                  self.rotate(-90)
                self.collision = False
                self.state_machine = SelectorState.IDLE
                
    def update(self, box :Box):
        # Permets de checker constamment les zones de détections du selector
        self.detectionZone.update(box)
        self.stateHandler(box)
        
    def boxEnteredBehavior(self, box):
        self.state_machine = SelectorState.RECEIVING
        self.currentBoxColor = box.getColor()
        if self.currentBoxColor == RED:
            exitZone = 'up'
        elif self.currentBoxColor == BLUE:
            exitZone = 'right'
        elif self.currentBoxColor == GREEN:
            exitZone = 'down'
        else:
            exitZone = 'left'
        self.resetExitZone()
        self.setExitZone(self.rect, exitZone)

    def boxExitedBehavior(self, box):
        self.state_machine = SelectorState.RESETTING

    def setEntryZone(self, selectorRect: pygame.Rect, entryZonePosition: str):
        if entryZonePosition == 'up':
            self.detectionZone.setEntryZone(pygame.Rect(selectorRect.left, selectorRect.bottom, selectorRect.width, self.DETECT_MARGIN))
        elif entryZonePosition == 'down':
            self.detectionZone.setEntryZone(pygame.Rect(selectorRect.left, selectorRect.top - self.DETECT_MARGIN, selectorRect.width, self.DETECT_MARGIN))
        elif entryZonePosition == 'right':
            self.detectionZone.setEntryZone(pygame.Rect(selectorRect.right, selectorRect.top, self.DETECT_MARGIN, selectorRect.height))
        elif entryZonePosition == 'left':
            self.detectionZone.setEntryZone(pygame.Rect(selectorRect.left - self.DETECT_MARGIN, selectorRect.top, self.DETECT_MARGIN, selectorRect.height))
        else:
            print("Invalid entry zone position")

    def setExitZone(self, selectorRect: pygame.Rect, exitZonePosition: str):
        if exitZonePosition == 'up':
            self.detectionZone.setExitZone(pygame.Rect(selectorRect.left, selectorRect.top - self.DETECT_MARGIN, selectorRect.width, self.DETECT_MARGIN))
        elif exitZonePosition == 'down':
            self.detectionZone.setExitZone(pygame.Rect(selectorRect.left, selectorRect.bottom, selectorRect.width, self.DETECT_MARGIN))
        elif exitZonePosition == 'right':
            self.detectionZone.setExitZone(pygame.Rect(selectorRect.right, selectorRect.top, self.DETECT_MARGIN, selectorRect.height))
        elif exitZonePosition == 'left':
            self.detectionZone.setExitZone(pygame.Rect(selectorRect.left - self.DETECT_MARGIN, selectorRect.top, self.DETECT_MARGIN, selectorRect.height))
        else:
            print("Invalid exit zone position")

    def resetExitZone(self):
        self.detectionZone.setExitZone(pygame.Rect(0, 0, 0, 0))  # Reset to an empty rect

    def getNearbyConveyors(self):
       cx, cy = self.getMiddle()
       nearby = []
       for c in Conveyor.conveyorsList:
           if c is self:
               continue
           c_mid_x, c_mid_y = c.getMiddle()
           dist = ((cx - c_mid_x)**2 + (cy - c_mid_y)**2)**0.5
           if dist <= self.RADIUS:
               nearby.append(c)
       return nearby
    
    def getFrontConveyor(self):
        angle = self.getAngle()
        cx, cy = self.getMiddle()

        closest = None
        min_dist = float("inf")

        for i,c in enumerate(Conveyor.conveyorsList):
            if c is self:
                continue

            x, y = c.getMiddle()

            # Facing UP
            if angle == 0 and abs(x - cx) < 3 and y < cy:
                dist = cy - y

            # Facing DOWN
            elif angle in (180, -180) and abs(x - cx) < 3 and y > cy:
                dist = y - cy

            # Facing RIGHT
            elif angle in (-90, 270) and abs(y - cy) < 3 and x > cx:
                dist = x - cx

            # Facing LEFT
            elif angle in (90, -270) and abs(y - cy) < 3 and x < cx:
                dist = cx - x

            else:
                continue

            # Keep closest one
            if dist < min_dist:
                min_dist = dist
                closest = c
        return closest
    
    def stopFrontConveyor(self):
        if self.getFrontConveyor():
            self.getFrontConveyor().stop()
     
    def stopFrontConveyorSection(self):
        frontConveyor = self.getFrontConveyor()           
        for c in Conveyor.conveyorsList:
            if c.getSection() == frontConveyor.getSection():
                c.stop()
            else:
                continue
    
    def activateFrontConveyorSection(self):
        frontConveyor = self.getFrontConveyor()
        for c in Conveyor.conveyorsList:
            if c.getSection() == frontConveyor.getSection():
                c.activate()
            else:
                break
            
    def activateFrontConveyor(self):
        if self.getFrontConveyor():
            self.getFrontConveyor().activate()

    def stopNearbyConveyors(self):
        for c in self.getNearbyConveyors():
            c.stop()

    def draw(self, screen):
        import pygame
        screen.blit(self.surface, self.rect)
        #pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)
        self.detectionZone.draw(screen)