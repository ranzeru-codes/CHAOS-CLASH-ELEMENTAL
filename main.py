import pygame
import time

from menu import menu
from game import Game


pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "CHAOS CLASH: ELEMENTAL"
)


# Loading Screen
def loading():

    font = pygame.font.Font(None, 60)

    for i in range(101):

        screen.fill((5, 10, 30))

        text = font.render(
            "CHAOS CLASH: ELEMENTAL",
            True,
            (255, 255, 255)
        )

        screen.blit(
            text,
            (250, 250)
        )

        pygame.draw.rect(
            screen,
            (0, 200, 255),
            (200, 350, i * 8, 30)
        )

        pygame.display.update()

        time.sleep(0.02)


loading()


# Main Game Loop
running = True

while running:

    choice = menu(screen)

    if choice == "START":

        game = Game(screen)
        game.run()


    elif choice == "QUIT":

        running = False


pygame.quit()
