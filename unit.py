import pygame


class Unit:


    def __init__(self,x,y,element):

        self.x=x
        self.y=y
        self.element=element

        self.level=1
        self.damage=10


    def upgrade(self):

        self.level += 1
        self.damage += 10



    def draw(self,screen):

        colors={

        "Flame":(255,80,0),
        "Hydro":(0,150,255),
        "Gale":(0,255,150),
        "Terra":(150,100,50),
        "Storm":(150,0,255),
        "Light":(255,255,100),
        "Dark":(80,0,100),
        "Neutral":(150,150,150)

        }


        pygame.draw.circle(
            screen,
            colors[self.element],
            (self.x,self.y),
            25
        )