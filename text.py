import pygame
from pygame import font
pygame.font.init()  # Initialize the font module
class Text():
    def __init__(self, position, text: str, font=None, size=12):
        self.position = position
        self.text = text
        self.size = size

        if font:
            self.font = pygame.font.SysFont(font, self.size)
        else:
            self.font = pygame.font.Font(None, self.size)


    def render(self, surface):
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, self.position)

