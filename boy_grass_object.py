from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Ball:
    def __init__(self):
        pass
    def draw(self):
        pass
    def update(self):
        pass

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
