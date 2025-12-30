import pygame
import assets
from settings import *
from Box import Box
from Conveyor import Conveyor
from Corner import Corner
from Selector import Selector
from DetectionZone import DetectionZone

#Lists
cornerList = []
conveyorTopList = []
conveyorMidList = []
conveyorBotList = []
selectorList = []
# screen and framerate variables
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #creating canva
clock = pygame.time.Clock()  # Creating clock

assets.load_assets()
DELTA_TIME = 0.1

# START CONVEYOR AND CORNER CREATION -----------------------------------------------------------------
conveyorStart = Conveyor(50,300,-90.0)
conveyorStart2 = Conveyor(0,300,-90.0)


# Creation of  vertical left conveyors
for i in range(0, TRACKS_WIDTH):
    conveyorTopList.append(Conveyor(100,300-50*(i+1),0))
    conveyorBotList.append(Conveyor(100,300+50*(i+1),180))

# Creation of horizontal conveyors
for i in range(0,TRACKS_LENGTH):
    conveyorTopList.append(Conveyor(150+50*i,300-50*(TRACKS_WIDTH+1),-90))
    conveyorMidList.append(Conveyor(150+50*i,300,-90))
    conveyorBotList.append(Conveyor(150+50*i,300+50*(TRACKS_WIDTH+1),-90))

# Creation of vertical right conveyors
for i in range(TRACKS_WIDTH,0,-1):
    conveyorTopList.append(Conveyor(150+50*TRACKS_LENGTH,300-50*i,-180))
    conveyorBotList.append(Conveyor(150+50*TRACKS_LENGTH,300+50*i,0))

# Create corner instances
cornerList = [
    Corner(100,250-50*TRACKS_WIDTH,0),                               #top left
    Corner(150+50*TRACKS_LENGTH,250-50*TRACKS_WIDTH,-90),             #top right
    Corner(150+50*TRACKS_LENGTH,350+50*TRACKS_WIDTH,-90,flip=True),   #bottom right
    Corner(100,350+50*TRACKS_WIDTH,-180,flip=True)                   #bottom left
    ]

#create list of Selector instances
selectorList = [Selector(100, 300, angle=90, entryZone='left')]
# END CONVEYOR AND CORNER CREATION -----------------------------------------------------------------


# START BOXES CREATION -----------------------------------------------------------------
boxes = [
    Box(90, 315, 0, 0, color=GREEN),
    Box(125, 400, 0, 0, color=BLUE),
    Box(125, 200, 0, 0, color=GREEN),
    Box(60, 315, 0, 0, color=RED),
    Box(0, 315, 0, 0, color=BLUE)

    ]
# END BOXES CREATION ------------------------------------------

# DRAWING SEQUENCE ------------------------------------------
def drawing_elements():
    screen.fill(pygame.Color(255,255,255))  # background color drawing in white
    for c in Conveyor.conveyorsList:
        c.draw(screen)

    for b in boxes:
        b.update(DELTA_TIME)
        b.draw(screen)
    pygame.display.flip()

def updateSelectors():
    for b in boxes:
        for s in selectorList:
            if b.collision(s) or b.rect.colliderect(s.detectionZone.entry_rect) or b.rect.colliderect(s.detectionZone.exit_rect):
                s.update(b)
                break


def conveyorListActivate(conveyorList):
    for c in conveyorList:
        c.activate()

def collisionChecker(conveyors, boxes):
    for box in boxes:
        box.setSpeed(0, 0)

        for conveyor in conveyors:
            if box.collision(conveyor) and conveyor.state == 1:
                conveyor.collisionHandler(box)
                break   
  
conveyorListActivate(Conveyor.conveyorsList)


# MAIN LOOP ------------------------------------------
running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False 
    collisionChecker(Conveyor.conveyorsList, boxes)
    updateSelectors()
    drawing_elements()
    DELTA_TIME = clock.tick(FPS)/1000
    DELTA_TIME = max(0.001,min(0.1, DELTA_TIME))
pygame.quit()
