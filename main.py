import pygame
import OpenGL.GL as gl
import imgui
from imgui.integrations.pygame import PygameRenderer
import sys
import os
import random

size = 1200, 800
pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("fruit bro")

imgui.create_context()

io = imgui.get_io()
io.display_size = size

renderer = PygameRenderer()

clock = pygame.time.Clock()

r_1to4 = random.randint(1, 4)
def background(number):
    backgrounds = {
        1:(0/255.0, 51/255.0, 34/255.0, 1), #dark green
        2:(123/255.0, 129/255.0, 32/255.0, 1.0), #yellow
        3:(51/255.0, 0/255.0, 102/255.0, 1.0), #purple
        4:(0/255.0, 0/255.0, 102/255.0, 1.0), #dark blue
    }
    gl.glClearColor(*backgrounds[number])


def main():
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        renderer.process_event(event)
    
    imgui.new_frame()
    renderer.process_inputs()

    imgui.begin("shop")

    imgui.text("hello")

    imgui.end()

    background(r_1to4)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imgui.render()
    renderer.render(imgui.get_draw_data())
    pygame.display.flip()
    clock.tick(60)

renderer.shutdown()
pygame.quit()