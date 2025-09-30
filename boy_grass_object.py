from pico2d import *
import random
def reset_world():
    pass

def update_world():
    pass


def render_world():
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
