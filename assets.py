import pygame

CONVEYOR_IMG = None
CORNER_IMG = None
BOX_IMG = None
SELECTOR_IMG = None

def load_assets():
    global CONVEYOR_IMG, CORNER_IMG, BOX_IMG, SELECTOR_IMG

    CONVEYOR_IMG = pygame.image.load(
        'img/conveyor.png'
    ).convert_alpha()

    CORNER_IMG = pygame.image.load(
        'img/corner.png'
    ).convert_alpha()

    BOX_IMG = pygame.image.load(
        'img/box.png'
    ).convert_alpha()

    SELECTOR_IMG = pygame.image.load(
        'img/selector.png'
    ).convert_alpha()