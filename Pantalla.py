from traceback import print_tb
import pygame
import sys
from pygame.locals import *
import random

class Pantalla():
    def __init__(self):
        pygame.font.init()
        self.my_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
        self.WINDOW_HEIGHT = 420
        self.WINDOW_WIDTH = 420
        self.BLOCSIZE = 20
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))