import pygame
import pygame_gui
import sys
import os
import random

pygame.init()

size = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("fruit bro")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(__file__)

rand_1to4 = random.randint(1, 4)
def background(number):
    backgrounds = {
        1:(0, 51, 34), #dark green
        2:(123, 129, 32), #yellow
        3:(51, 0, 102), #purple
        4:(0, 0, 102), #dark blue
    }
    screen.fill(backgrounds.get(number))

rand_1to3 = random.randint(1, 3)
rocks_list = []
def rock(number):
    rock1_path = os.path.join(BASE_DIR, "images", "rock1.png") #X=101 , Y=64
    rock2_path = os.path.join(BASE_DIR, "images", "rock2.png") #X=101 , Y=64
    rock3_path = os.path.join(BASE_DIR, "images", "rock3.png") #X=101 , Y=64
    rock1_img = pygame.image.load(rock1_path).convert_alpha()
    rock2_img = pygame.image.load(rock2_path).convert_alpha()
    rock3_img = pygame.image.load(rock3_path).convert_alpha()
    rocks = {
        1:rock1_img,
        2:rock2_img,
        3:rock3_img,
    }
    for i in range(37):
        rock_x = random.randint(0, 1099)
        rock_y = random.randint(0, 736)
        rocks_list.append((rocks.get(number), (rock_x, rock_y)))

def show_rock():
    for rock_img, pos in rocks_list:
        screen.blit(rock_img, pos)


def main():
    pass

rock(rand_1to3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background(rand_1to4)
    show_rock()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()