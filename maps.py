import pygame


def select_map(screen):

    font = pygame.font.Font(None,50)

    while True:

        screen.fill((15,20,50))

        title = font.render(
            "SELECT MAP",
            True,
            (255,255,255)
        )

        screen.blit(title,(450,100))


        maps = [
            pygame.Rect(150,300,220,100),
            pygame.Rect(490,300,220,100),
            pygame.Rect(830,300,220,100)
        ]


        for i,button in enumerate(maps):

            pygame.draw.rect(
                screen,
                (50,120,220),
                button
            )

            text = font.render(
                f"MAP {i+1}",
                True,
                (255,255,255)
            )

            screen.blit(
                text,
                (button.x+50,button.y+25)
            )


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                for i,b in enumerate(maps):

                    if b.collidepoint(event.pos):
                        return i+1


        pygame.display.update()