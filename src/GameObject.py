import pygame
from pygame.locals import *

class GameObject():
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        objectRect = Rect(self.x_pos, self.y_pos, self.width, self.height)
        drawnRect = pygame.draw.rect(screen, self.color, objectRect, 0, 10, 10, 10)
        return drawnRect
        
    # Get X and Y position
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    
    # Set X and Y position
    def setX(self, x):
        self.x_pos = x
    def setY(self, y):
        self.y_pos = y