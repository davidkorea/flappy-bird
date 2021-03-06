import pygame
from pygame.locals import *
from sys import exit

BACKGROUND_PATH = './assets/sprites/background-black.png'
PIPE_PATH = './assets/sprites/pipe-green.png'
BASE_PATH = './assets/sprites/base.png'
PLAYER_PATH = (
    './assets/sprites/redbird-upflap.png',
    './assets/sprites/redbird-midflap.png',
    './assets/sprites/redbird-downflap.png'
)
SCREENWIDTH = 288
SCREENHEIGHT = 512
IMAGES = {}

pygame.init()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Flappy Bird')
IMAGES['background'] = pygame.image.load(BACKGROUND_PATH).convert()
IMAGES['base'] = pygame.image.load(BASE_PATH).convert_alpha()
IMAGES['bird'] = (
    pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
    pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
    pygame.image.load(PLAYER_PATH[2]).convert_alpha()
)
IMAGES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE_PATH).convert_alpha(), 180),
    pygame.image.load(PIPE_PATH).convert_alpha()
)

PIPE_WIDTH = IMAGES['pipe'][0].get_width()
PIPE_HEIGHT = IMAGES['pipe'][0].get_height()

x = 1/2 * SCREENWIDTH
y = 1/2 * SCREENHEIGHT
move_x = 0
move_y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_DOWN:
                move_y = 1
            elif event.key == K_UP:
                move_y = -1
        # y-axis 0 -> +inf from top to buttom, so K_UP = -3
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
    x = x + move_x
    y = y + move_y
    if x > SCREENWIDTH:
        x = 0
    elif x < 0:
        x = SCREENWIDTH
    if y > SCREENHEIGHT:
        y = 0
    elif y < 0:
        y = SCREENHEIGHT

    SCREEN.blit(IMAGES['background'],(0,0))
    SCREEN.blit(IMAGES['pipe'][0], (0,0))
    SCREEN.blit(IMAGES['pipe'][1], (0,SCREENHEIGHT-PIPE_HEIGHT))

    SCREEN.blit(IMAGES['bird'][1], (x, y))

    pygame.display.update()



