import pygame


class Game:

    def __init__(self, screen):
        self.screen = screen


    def run(self):

        running = True

        while running:

            self.screen.fill((20,80,50))

            font = pygame.font.Font(None,60)

            text = font.render(
                "GAME STARTED",
                True,
                (255,255,255)
            )

            self.screen.blit(
                text,
                (400,300)
            )


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running=False


            pygame.display.update()