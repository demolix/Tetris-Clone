import pygame as pg

# colors used
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
PURPLE = (128, 0 , 128)
GREY = (185, 185, 185)
YELLOW = (175, 175,  20)

COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)


#block stats
BOXSIZE = 20

# game window
BOARDWIDTH = 10
BOARDHEIGHT = 20
PLATFORM_HEIGHT = 50
WIDTH = 300
HEIGHT = 600 + PLATFORM_HEIGHT
GAME_NAME = "Tetris"
FPS = 4
MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1
BLANK = '.'
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BGCOLOR = BLACK
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5



PLATFORM_WIDTH = WIDTH