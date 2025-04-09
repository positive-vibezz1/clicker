import pygame

class Sprite():
    def __init__(self, position, imagepath=None, colour=(255,0,0), size=(50,50), sheet_info=None):
        self.position = position
        self.colour = colour
        self.size = size
        self.sheet_info = sheet_info
        if imagepath:
            self.image = pygame.image.load(imagepath).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
        else:
            self.image = pygame.Surface(size)
            self.image.fill(colour)
    def render(self, screen, index=0):
        x,y = self.sheet_info[index]
        digit_surface = self.image.subsurface(pygame.Rect(x, y, self.size[0], self.size[1]))

        screen.blit(digit_surface, self.position)

