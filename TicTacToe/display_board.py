import pygame
pygame.init()
display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tic, Tac, Toe, powered by AI')

crashed = False
white = (250,250,250)
xImg = pygame.image.load('xpng.png')
oImg = pygame.image.load('o_png.png')
planszaImg = pygame.image.load('332570.png')





def square1(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (20,20))
    elif ktory == 2:
        gameDisplay.blit(oImg, (20,20))

def square2(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (225,20))
    elif ktory == 2:
        gameDisplay.blit(oImg, (225,20))

def square3(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (420,20))
    elif ktory == 2:
        gameDisplay.blit(oImg, (420,20))

def square4(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (20,230))
    elif ktory == 2:
        gameDisplay.blit(oImg, (20,230))

def square5(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (225,230))
    elif ktory == 2:
        gameDisplay.blit(oImg, (225,230))

def square6(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (420,230))
    elif ktory == 2:
        gameDisplay.blit(oImg, (420,230))

def square7(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (20,420))
    elif ktory == 2:
        gameDisplay.blit(oImg, (20,420))

def square8(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (225,420))
    elif ktory == 2:
        gameDisplay.blit(oImg, (225,420))

def square9(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (420,420))
    elif ktory == 2:
        gameDisplay.blit(oImg, (420,420))

def board():
    gameDisplay.blit(planszaImg, (0,0))


def gameImage(planszaAkt):
    gameDisplay.fill(white)
    board()
    if planszaAkt[0] == 'X':
        square1(1)
    elif planszaAkt[0] == 'O':
        square1(2)
    else:
        square1(3)

    if planszaAkt[1] == 'X':
        square2(1)
    elif planszaAkt[1] == 'O':
        square2(2)
    else:
        square2(3)

    if planszaAkt[2] == 'X':
        square3(1)
    elif planszaAkt[2] == 'O':
        square3(2)
    else:
        square3(3)

    if planszaAkt[3] == 'X':
        square4(1)
    elif planszaAkt[3] == 'O':
        square4(2)
    else:
        square4(3)

    if planszaAkt[4] == 'X':
        square5(1)
    elif planszaAkt[4] == 'O':
        square5(2)
    else:
        square5(3)

    if planszaAkt[5] == 'X':
        square6(1)
    elif planszaAkt[5] == 'O':
        square6(2)
    else:
        square6(3)

    if planszaAkt[6] == 'X':
        square7(1)
    elif planszaAkt[6] == 'O':
        square7(2)
    else:
        square7(3)

    if planszaAkt[7] == 'X':
        square8(1)
    elif planszaAkt[7] == 'O':
        square8(2)
    else:
        square8(3)

    if planszaAkt[8] == 'X':
        square9(1)
    elif planszaAkt[8] == 'O':
        square9(2)
    else:
        square9(3)


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameImage(['X', ' ', 'O', 'O', 'X', 'O', ' ', ' ', ' '])

    pygame.display.update()
