from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Ball:
    def __init__(self):
        self.size=random.choice([21,41])
        if self.size==21:
            self.image=load_image('ball21x21.png')
        else:
            self.image=load_image('ball41x41.png')
        self.x=random.randint(0,800)
        self.y=599
        self.speed=random.randint(5,20)

    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        self.y-=self.speed

        if self.y<=self.size//2+50:
            self.y=self.size//2+50
            self.speed=0

def reset_world():
    global grass,balls
    grass=Grass()
    balls=[Ball() for _ in range(20)]
    pass

def update_world():
    for ball in balls:
        ball.update()
    pass


def render_world():
    grass.draw()
    for ball in balls:
        ball.draw()
    pass

open_canvas()

reset_world()

while True:
    clear_canvas()
    update_world()
    render_world()
    update_canvas()
    delay(0.05)
close_canvas()
