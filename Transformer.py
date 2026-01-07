from Selector import Selector
from SectionType import SectionType
from SelectorState import SelectorState
from settings import WAIT_TIME
import assets
class Transformer(Selector):
    transformerList = []
    def __init__(self, x, y, angle=0, scale=0.1): 
        self.base_img = assets.TRANSFORMER_IMG.copy() 
        super().__init__(x, y, angle, scale, entryZone='left')
        self.setExitZone(self.rect, 'right')
        print("Transformer exit_rect after set:", self.detectionZone.exit_rect)
        self.section = SectionType.TRANSFORMER
        self.startTimer = 0
        self.transformerList.append(self)


    def stateHandler(self, box):
        print(self.getStateMachine())
        import pygame
        match self.state_machine:
            case SelectorState.IDLE:
                self.activateFrontConveyorSection()

            case SelectorState.RECEIVING:
                self.moveToCenter(box)
                if self.collision:
                    self.stopFrontConveyorSection()
                if self.isBoxCentered(box): 
                    self.startTimer = pygame.time.get_ticks()
                    self.state_machine = SelectorState.WAITTING

            case SelectorState.WAITTING:
                box.setSpeed(0,0)
                if pygame.time.get_ticks()-self.startTimer > WAIT_TIME:
                    self.state_machine = SelectorState.ROTATING 
                
            case SelectorState.ROTATING:
                self.rotate(180)
                self.state_machine = SelectorState.SENDING

            case SelectorState.SENDING:
                self.moveToFacingDirection(box)
            
            case SelectorState.RESETTING:
                self.rotate(-180)
                self.collision = False
                self.state_machine = SelectorState.IDLE

    def boxEnteredBehavior(self, box):
        print("Box received")
        self.state_machine = SelectorState.RECEIVING
        self.setExitZone(self.rect,'right')

    