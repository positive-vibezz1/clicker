import pygame

class Sprite():
    def __init__(self, position, imagepath=None, colour=(255,0,0), size=(64,64), sheet_info=None, sprite_size=(64, 64)):

        self.position = position
        self.colour = colour
        self.size = size
        self.sheet_info = sheet_info
        self.sprite_size = sprite_size
        if imagepath:
            self.image = pygame.image.load(imagepath).convert_alpha()
        else:
            self.image = pygame.Surface(self.sprite_size)
            self.image.fill(colour)

        self.rect = pygame.Rect(self.position, self.size)
    def render(self, screen, index=0):
        x,y = self.sheet_info[index]
        sprite_rect = pygame.Rect(x, y, self.sprite_size[0], self.sprite_size[1])

        digit_surface = self.image.subsurface(sprite_rect)
        digit_surface = self.image.subsurface(pygame.Rect(x, y, self.sprite_size[0], self.sprite_size[1]))
        scaled_surface = pygame.transform.scale(digit_surface, self.size)

        screen.blit(scaled_surface, self.position)

