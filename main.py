import pygame
import pygame_gui
from button import Button
import sys
import os
import random

pygame.init()

size = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("fruit bro")

clock = pygame.time.Clock()

running = True

BASE_DIR = os.path.dirname(__file__)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

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
    rock1_path = os.path.join(BASE_DIR, "assets", "rock1.png") #X=101 , Y=64
    rock2_path = os.path.join(BASE_DIR, "assets", "rock2.png") #X=101 , Y=64
    rock3_path = os.path.join(BASE_DIR, "assets", "rock3.png") #X=101 , Y=64
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

class Enemy:
    def __init__(self, img, damage, speed):
        self.img = img
        self.damage = damage
        self.speed = speed

def play():
    rock(rand_1to3)

    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background(rand_1to4)
        show_rock()
        pygame.display.flip()
        clock.tick(60)

mmbg_path = os.path.join(BASE_DIR, "assets", "mm_Background.png")
mmbg_img = pygame.image.load(mmbg_path)
def main_menu():
    global running
    while running:
        screen.blit(mmbg_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False

        pygame.display.flip()


def main():
    main_menu()
    play()

    pygame.quit()

if __name__ == "__main__":
    main()