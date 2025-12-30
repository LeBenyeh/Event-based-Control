import pygame
from Box import Box
from typing import Optional


class DetectionZone:
    def __init__(self, selector, margin=20):
        # Use a runtime reference to selector; avoid importing Selector class to
        # prevent circular imports. The annotation was removed for that reason.
        self.selector = selector
        self.margin = margin

        self.entry_rect: Optional[pygame.Rect] = None
        self.exit_rect: Optional[pygame.Rect] = None

        self.tracked_box: Optional[Box] = None  # Box actuellement suivie

    def update(self, box: Box):
        # If entry or exit rects not defined, nothing to do
        if self.entry_rect is None or self.exit_rect is None:
            return

        # If no box tracked -> check entry
        if self.tracked_box is None:
            if self.entry_rect.colliderect(box.rect):
                self.tracked_box = box  # Enregistrement de la box suivie
                self.selector.boxEnteredBehavior(box)
        # If a box is tracked -> check exit
        elif self.tracked_box == box:
            if self.isBoxInExitZone(box):
                self.selector.boxExitedBehavior(box)
                self.tracked_box = None

    def setEntryZone(self, rect: pygame.Rect):
        # store a copy to avoid accidental external mutations
        self.entry_rect = rect.copy()

    def setExitZone(self, rect: pygame.Rect):
        self.exit_rect = rect.copy()

    def draw(self, screen):
        if self.entry_rect:
            pygame.draw.rect(screen, (0, 255, 0), self.entry_rect, 2)
        if self.exit_rect:
            pygame.draw.rect(screen, (255, 0, 0), self.exit_rect, 2)

    def isBoxInExitZone(self, box: Box) -> bool:
        return bool(self.exit_rect and self.exit_rect.colliderect(box.rect))

