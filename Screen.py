from traceback import print_tb
import pygame
import sys
from pygame.locals import *
import random

class Screen():
    def __init__(self):
        pygame.font.init()
        self.startScreen()
        self.my_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
        self.WINDOW_HEIGHT = 420
        self.WINDOW_WIDTH = 420
        self.BLOCSIZE = 20