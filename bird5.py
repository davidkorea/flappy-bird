import pygame
from pygame.locals import *
from sys import exit
import random

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
BASEY = SCREENHEIGHT * 0.79
PIPEGAPSIZE = 100


FPS = 30
FPSCLOCK = pygame.time.Clock()


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
PLAYER_WIDTH = IMAGES['bird'][0].get_width()
PLAYER_HEIGHT = IMAGES['bird'][0].get_height()
# x = 1/2 * SCREENWIDTH
# y = 1/2 * SCREENHEIGHT
# move_x = 0
# move_y = 0

flap = 0

def getRandomPipe():
    gapYs = [10,30,40,60,90,110,130,160,190]
    index = random.randint(0, len(gapYs)-1)
    gapY = gapYs[index]
    gapY += int(BASEY * 0.2)
    pipeX = SCREENWIDTH + 10
    return [
        {'x': pipeX, 'y': gapY-PIPE_HEIGHT},
        {'x': pipeX, 'y': gapY+PIPEGAPSIZE}
    ]

pipeVelX = -4
playerVelY = 0
playerMaxVelY = 10
playerMinVelY = -8
playerAccY = 2
playerflapAcc = -3
playerflapped = False
playery = int((SCREENHEIGHT - PLAYER_HEIGHT) / 2)




newPipe1 = getRandomPipe()
upperPipes = [
    {'x': SCREENWIDTH, 'y': newPipe1[0]['y']},
]
lowerPipes = [
    {'x': SCREENWIDTH, 'y': newPipe1[1]['y']},
]



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -3
            elif event.key == K_RIGHT:
                move_x = 3
            elif event.key == K_DOWN:
                move_y = 3
            elif event.key == K_UP:
                move_y = -3
        # y-axis 0 -> +inf from top to buttom, so K_UP = -3
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0

    for upipe, lpipe in zip(upperPipes, lowerPipes):
        upipe['x'] += pipeVelX
        lpipe['x'] += pipeVelX
        # SCREEN.blit(IMAGES['pipe'][0], (upipe['x'], upipe['y']))
        # SCREEN.blit(IMAGES['pipe'][1], (lpipe['x'], lpipe['y']))
        # why can not show pipes here directly?????

    if 0 < upperPipes[0]['x'] < 5:
        newPipe = getRandomPipe()
        upperPipes.append(newPipe[0])
        lowerPipes.append(newPipe[1])

    if upperPipes[0]['x'] < - PIPE_WIDTH:
        upperPipes.pop(0)
        lowerPipes.pop(0)

    input_actions = random.randint(0,6)
    if input_actions % 3 == 0:
        playerVelY = playerflapAcc
        playerflapped = True


    if playerVelY < playerMaxVelY and not playerflapped:
        playerVelY += playerAccY
    if playerflapped:
        playerflapped = False

    playery += min(playerVelY, BASEY - playery - PLAYER_HEIGHT)

    if playery < 0:
        playery = 0

    # x = x + move_x
    x = 1/2 * SCREENWIDTH
    # y = y + move_y
    # if x > SCREENWIDTH:
    #     x = 0
    # elif x < 0:
    #     x = SCREENWIDTH
    # if y > SCREENHEIGHT:
    #     y = 0
    # elif y < 0:
    #     y = SCREENHEIGHT



    SCREEN.blit(IMAGES['background'],(0,0))
    # SCREEN.blit(IMAGES['pipe'][0], (0,0))
    # SCREEN.blit(IMAGES['pipe'][1], (0,SCREENHEIGHT-PIPE_HEIGHT))
    # 显示水管
    for uPipe, lPipe in zip(upperPipes, lowerPipes):
        SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'],uPipe['y']))
        SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'],lPipe['y']))


    SCREEN.blit(IMAGES['bird'][flap], (x, playery))
    flap = flap + 1
    if flap % 3 == 0:
        flap = 0


    pygame.display.update()
    FPSCLOCK.tick(FPS)



