import random


class Car(object):
    speed = 0
    color = ''
    name = ''
    is_police = False
    def __init__(self, color, name):
        self.color = color
        self.name = name
    def go(self):
        self.speed += random.randint(0, 10)
        print('rides')
    def stop(self):
        self.speed = 0
        print('is worth')
    def turn(self, direction):
        print(f'the car turned on {direction}')
    def show_speed(self):
        print(f'current speed: {self.speed}')