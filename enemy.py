import pygame


class Enemy:


    def __init__(self):

        self.x=100
        self.y=350

        self.hp=100
        self.speed=2


    def move(self):

        self.x += self.speed



    def draw(self,screen):

        pygame.draw.circle(
            screen,
            (200,0,0),
            (self.x,self.y),
            25
        )