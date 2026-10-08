import time
from enemy import Enemy


class Wave:


    def __init__(self):

        self.wave_number = 1
        self.enemies = []


    def start_wave(self):

        amount = self.wave_number * 5


        for i in range(amount):

            enemy = Enemy()

            self.enemies.append(enemy)



    def next_wave(self):

        self.wave_number += 1
        self.enemies.clear()



    def update(self):

        for enemy in self.enemies:

            enemy.move()



    def draw(self,screen):

        for enemy in self.enemies:

            enemy.draw(screen)