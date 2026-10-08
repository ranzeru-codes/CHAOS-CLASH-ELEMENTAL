import pygame


def create_button(
screen,text,x,y):


    rect=pygame.Rect(
    x,y,250,80
    )


    pygame.draw.rect(
    screen,
    (50,100,200),
    rect
    )


    font=pygame.font.Font(
    None,50
    )


    label=font.render(
    text,
    True,
    (255,255,255)
    )


    screen.blit(
    label,
    (x+40,y+15)
    )


    return rect



def menu(screen):

    while True:

        screen.fill(
        (20,20,60)
        )


        start=create_button(
        screen,
        "START",
        475,250
        )


        quit=create_button(
        screen,
        "QUIT",
        475,380
        )


        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:

                if start.collidepoint(
                event.pos):

                    return "START"


                if quit.collidepoint(
                event.pos):

                    return "QUIT"


        pygame.display.update()
