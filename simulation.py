import pygame
import assets
from settings import *
from Box import Box
from Conveyor import Conveyor
from Corner import Corner
from Selector import Selector
from SectionType import SectionType
from Transformer import Transformer
from Dispenser import Dispenser

#Lists

# screen and framerate variables
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #creating canva
clock = pygame.time.Clock()  # Creating clock

assets.load_assets()
DELTA_TIME = 0.1
STARTX = 100
STARTY = 100

# START CONVEYOR AND CORNER CREATION -----------------------------------------------------------------
conveyorStart = Conveyor(50+STARTX,300+STARTY,angle=-90.0)
conveyorStart.setSection(SectionType.CONVEYOR_START)
conveyorStart2 = Conveyor(0+STARTX,300+STARTY,-90.0)
conveyorStart2.setSection(SectionType.CONVEYOR_START)



# Creation of  vertical left conveyors
for i in range(0, TRACKS_WIDTH):
    Conveyor(100+STARTX,300-50*(i+1)+STARTY,0).setSection(SectionType.CONVEYOR_TOP)
    Conveyor(100+STARTX,300+50*(i+1)+STARTY,180).setSection(SectionType.CONVEYOR_BOT)

# Creation of horizontal conveyors
for i in range(0,TRACKS_LENGTH):
    if i == TRACKS_LENGTH - 3:
        Transformer(150+50*i+STARTX,300-50*(TRACKS_WIDTH+1)+STARTY,angle=90)
        Transformer(150+50*i+STARTX,300+STARTY,angle=90)
        Transformer(150+50*i+STARTX,300+50*(TRACKS_WIDTH+1)+STARTY,angle=90)
    elif i > TRACKS_LENGTH - 3: 
        Conveyor(150+50*i+STARTX,300-50*(TRACKS_WIDTH+1)+STARTY,-90).setSection(SectionType.CONVEYOR_TOP2)
        Conveyor(150+50*i+STARTX,300+STARTY,-90).setSection(SectionType.CONVEYOR_MID2)
        Conveyor(150+50*i+STARTX,300+50*(TRACKS_WIDTH+1)+STARTY,-90).setSection(SectionType.CONVEYOR_BOT2)
    else : 
        Conveyor(150+50*i+STARTX,300-50*(TRACKS_WIDTH+1)+STARTY,-90).setSection(SectionType.CONVEYOR_TOP)
        Conveyor(150+50*i+STARTX,300+STARTY,-90).setSection(SectionType.CONVEYOR_MID)
        Conveyor(150+50*i+STARTX,300+50*(TRACKS_WIDTH+1)+STARTY,-90).setSection(SectionType.CONVEYOR_BOT)


# Creation of vertical right conveyors
for i in range(TRACKS_WIDTH,0,-1):
    Conveyor(150+50*TRACKS_LENGTH+STARTX,300-50*i+STARTY,-180).setSection(SectionType.CONVEYOR_TOP)
    Conveyor(150+50*TRACKS_LENGTH+STARTX,300+50*i+STARTY,0).setSection(SectionType.CONVEYOR_BOT)

# Create corner instances
Corner(100+STARTX,250-50*TRACKS_WIDTH+STARTY,0).setSection(SectionType.CONVEYOR_TOP)                               #top left
Corner(150+50*TRACKS_LENGTH+STARTX,250-50*TRACKS_WIDTH+STARTY,-90).setSection(SectionType.CONVEYOR_TOP)            #top right
Corner(150+50*TRACKS_LENGTH+STARTX,350+50*TRACKS_WIDTH+STARTY,-90,flip=True).setSection(SectionType.CONVEYOR_BOT)   #bottom right
Corner(100+STARTX,350+50*TRACKS_WIDTH+STARTY,-180,flip=True).setSection(SectionType.CONVEYOR_BOT)                  #bottom left

#create list of Selector instances
Selector(100+STARTX, 300+STARTY, angle=90, entryZone='left')
# END CONVEYOR AND CORNER CREATION -----------------------------------------------------------------

#START DISPENSER CREATION ------------------------- 
dispenser = Dispenser(STARTX-50, 300+STARTY, angle=-90)

button_dispenser = pygame.Rect(0,0,200,100)
#END DISPENSER CREATION -----------------------------

# DRAWING SEQUENCE ------------------------------------------
def drawing_elements():
    screen.fill(pygame.Color(255,255,255))  # background color drawing in white
    for c in Conveyor.conveyorsList:
        c.draw(screen)
    
    for t in Transformer.transformerList:
        t.draw(screen)

    for b in Box.boxList:
        b.update(DELTA_TIME)
        b.draw(screen)

    pygame.draw.rect(screen, BLUE, button_dispenser)
    font = pygame.font.SysFont(None, 36)
    text = font.render("Dispense", True,BLACK)
    text_rect = text.get_rect(center=button_dispenser.center)
    screen.blit(text, text_rect)
    pygame.display.flip()

def updateSelectors():
    for b in Box.boxList:
        for s in Selector.selectorList:
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
        elif events.type == pygame.MOUSEBUTTONDOWN:
            if button_dispenser.collidepoint(events.pos):
                dispenser.dispense()
    collisionChecker(Conveyor.conveyorsList, Box.boxList)
    updateSelectors()
    drawing_elements()

    DELTA_TIME = clock.tick(FPS)/1000
    DELTA_TIME = max(0.001,min(0.1, DELTA_TIME))
pygame.quit()
