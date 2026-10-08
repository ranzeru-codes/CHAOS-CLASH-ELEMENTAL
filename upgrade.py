import pygame


def upgrade_menu(screen,unit):

    font=pygame.font.Font(None,40)


    box=pygame.Rect(
        900,400,250,150
    )


    pygame.draw.rect(
        screen,
        (30,30,50),
        box
    )


    text=font.render(
        "UPGRADE",
        True,
        (255,255,255)
    )


    screen.blit(
        text,
        (930,430)
    )


    mouse=pygame.mouse.get_pos()


    if box.collidepoint(mouse):

        if pygame.mouse.get_pressed()[0]:

            unit.upgrade()