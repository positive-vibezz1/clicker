import pygame
from button import Buttons
from text import Text
from sprite import Sprite


class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("clicker")


    def update(self):
        pygame.display.flip()

    def clear(self):
        self.screen.fill((0, 0, 0))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    window = Window(800, 600)

    number = 1
    upgrade_one = 0

    number_mod = number + upgrade_one

    UO_checknumber = 10
    sprite_width = 64

    sheet_info = [(i * sprite_width, 0) for i in range(10)]


    while True:
        """ put everything under this line """
        window.clear()

        """ put all rect widgets here """
        main_button = Buttons((255, 0, 0), 350, 250, 50, 50)
        upgrade_one_button = Buttons((0, 255, 0), 600, 100, 50, 50)

        """ put all text here """
        main_text = Text((10, 10), str(number), "arial", 24)

        """ put sprites here """
        main_sprite = Sprite((200, 100), r"Numbers\number_sprite.png", (255,0,0), (200, 50),sheet_info=sheet_info)
        # main_sprite = Sprite((200, 100), r"Numbers\number_sprite.png", (255,0,0), (200, 50),sheet_info=sheet_info)

        get_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_button.rect.collidepoint(get_mouse_pos):
                    number += number_mod
                    print(f" number total {number}")
                if number >= UO_checknumber and upgrade_one_button.rect.collidepoint(get_mouse_pos):
                    upgrade_one += 1
                    print(f"upgrade {upgrade_one}")

        """ button widgets here """
        main_button.draw(window.screen)
        upgrade_one_button.draw(window.screen)

        """ text widgets here"""
        main_text.render(window.screen)

        """ rendered sprites here """

        
        def sprite_render():
            index = 0
            for index, (x,y) in enumerate(main_sprite.sheet_info):
                if index == upgrade_one:
                    main_sprite.position = (x, y)
                    main_sprite.render(window.screen, index)
                    break


        sprite_render()


        clock.tick(60)

        """ dont put anything under this line """
        window.update()


if __name__ == "__main__":
    main()
