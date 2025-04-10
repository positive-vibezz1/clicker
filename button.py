import pygame

class Buttons():
    def __init__(self, colour, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
