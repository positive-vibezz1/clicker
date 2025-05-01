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


    number_mod = 1 + upgrade_one

        # upgrade button worth
    UO_checknumber = 10

    sprite_width = 64

    sheet_info = [(i * sprite_width, 0) for i in range(10)]



    while True:

        """ put everything under this line """
        window.clear()

        """ put rect here """
        main_button = Buttons((255, 0, 0), 350, 250, 50, 50)
        upgrade_one_button = Buttons((0, 255, 0), 600, 100, 50, 50)

        """ put text here """
        main_text = Text((10, 10), str(number), "arial", 36)
        upgrade_one_text = Text((600, 50), str(upgrade_one), "arial", 36)
        total_click_amount = Text((10, 50), str(f"you have {number_mod} oil per click"), "arial", 36)

        """ put sprites here """
        # main_sprite = Sprite((200, 100), r"Numbers\number_sprite.png", (255,0,0), (200, 50),sheet_info=sheet_info)
        button_sprite = Sprite((350, 250), r"data\sprites\oil_rig_inverted.png", (255,0,0), size=(128,128),sheet_info=sheet_info)
        upgrade_one_button_sprite = Sprite((625, 65), r"data\sprites\oil_outline.png", (255,0,0), size=(64,64),sheet_info=sheet_info)
        # main_sprite = Sprite((200, 100), r"Numbers\number_sprite.png", (255,0,0), (200, 50),sheet_info=sheet_info)

        get_mouse_pos = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_sprite.rect.collidepoint(get_mouse_pos):
                    number = number + number_mod
                    print(f"number mod {number_mod}")
                    print(f"upgrade {upgrade_one}")
                    print(f"total {number}")
                    print(f"mouse pos {get_mouse_pos}")
                if number >= UO_checknumber and upgrade_one_button_sprite.rect.collidepoint(get_mouse_pos):
                    upgrade_one += 1
                    number_mod = upgrade_one + 1
                    if number > 50:
                        UO_checknumber += 10
                    elif number > 100:
                        UO_checknumber += 50


        """ button widgets here """
        #main_button.draw(window.screen)
        #upgrade_one_button.draw(window.screen)

        """ text widgets here"""
        main_text.render(window.screen)
        upgrade_one_text.render(window.screen)
        total_click_amount.render(window.screen)

        """ rendered sprites here """
        # sprite_render()
        button_sprite.render(window.screen, 0)
        upgrade_one_button_sprite.render(window.screen, 0)


        clock.tick(60)

        """ dont put anything under this line """
        window.update()


if __name__ == "__main__":
    main()
