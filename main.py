from msilib import CAB
import random
import sys
from turtle import bgcolor
import pygame
from pygame.locals import *

def newRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

pygame.init()
pygame.display.set_caption("Game Base")
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = newRandomColor()
motion = [0, 0]
joyStickDeadZone = 0.5

player_auto_random = False
bg_auto_random = False
cantLook = False

bg_color = (0, 0, 0)

while True:
    if player_auto_random:
        my_square_color = newRandomColor()

    if bg_auto_random:
        bg_color = newRandomColor()

    if cantLook:
        my_square_color = newRandomColor()
        bg_color = newRandomColor()

    screen.fill(bg_color)
    
    pygame.draw.rect(screen, my_square_color, my_square)
    if abs(motion[0]) < joyStickDeadZone:
        motion[0] = 0
    if abs(motion[1]) < joyStickDeadZone:
        motion[1] = 0
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10

    if my_square.x < 0: 
        my_square.x = 0
    if my_square.x + my_square.width > 500: 
        my_square.x = 500 - my_square.width
    if my_square.y < 0: 
        my_square.y = 0
    if my_square.y + my_square.height > 500: 
        my_square.y = 500 - my_square.height

    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            # Move player with ABXY
            if event.button == 0: # A
                my_square_color = newRandomColor()
            if event.button == 3: # Y
                player_auto_random = not player_auto_random

            if event.button == 7: # Menu
                cantLook = not cantLook
                
        if event.type == JOYAXISMOTION:
            # Move player with Left stick
            if event.axis < 2:
                motion[event.axis] = event.value

        if event.type == JOYHATMOTION:
            # Left D-PAD button
            if event.value == (-1, 0):
                bg_color = newRandomColor()
            if event.value == (1, 0):
                bg_auto_random = not bg_auto_random

        print(event)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)