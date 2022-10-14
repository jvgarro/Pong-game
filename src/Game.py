from turtle import Screen
import pygame
import sys
from pygame.locals import *
import random

class GameObject():
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        ballRect = Rect(self.x_pos, self.y_pos, self.width, self.height)
        objectRect = pygame.draw.rect(screen, self.color, ballRect, 0, 10, 10, 10)
        return objectRect
        
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
class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.my_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
        self.WINDOW_HEIGHT = 420
        self.WINDOW_WIDTH = 420
        self.CLOCK = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        # Scores for player 1 and 2
        self.scores = [0, 0]
        self.main_menu = True
        # self.start = False
        # self.velocity = [10, 1]
        # self.begin_text = 'Press SPACE to start'
        self.ball = GameObject(300, 200, 20, 20, 'pink')
        self.pad1 = GameObject(0, 200, 10, 60, 'maroon3')
        self.pad2 = GameObject(410, 200, 10, 60, 'maroon3')
        self.setDefaultValues()
        self.main()
    
    def setDefaultValues(self):
        self.ball.setX(200)
        self.ball.setY(200)
        self.start = False
        self.velocity = [10, 1]
        self.begin_text = 'Press SPACE to start'
        self.pad1.setY(200)
        self.pad2.setY(200)

    def drawObjects(self):
        global ballRect, pad1Rect, pad2Rect
        score_surface = self.my_font.render(str(self.scores[0]) +' :SCORE: ' + str(self.scores[1]), False, 'White')
        self.SCREEN.blit(score_surface, (120, 0))
        begin_surface = self.my_font.render(str(self.begin_text), False, 'White')
        self.SCREEN.blit(begin_surface, (60, 120))
        ballRect = self.ball.draw(self.SCREEN)
        pad1Rect = self.pad1.draw(self.SCREEN)
        pad2Rect = self.pad2.draw(self.SCREEN)
        
    def defineKeyBindings(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pad1.getY() > 0:
            self.pad1.setY(self.pad1.getY() - 5)
        if keys[pygame.K_s] and self.pad1.getY() < self.WINDOW_HEIGHT - 60:
            self.pad1.setY(self.pad1.getY() + 5)
        if keys[pygame.K_UP] and self.pad2.getY() > 0:
            self.pad2.setY(self.pad2.getY() - 5)
        if keys[pygame.K_DOWN] and self.pad2.getY() < self.WINDOW_HEIGHT - 60:
            self.pad2.setY(self.pad2.getY() + 5)
    
    def checkCollisions(self, ball, pad):
        if ball.colliderect(pad):
            self.velocity[0] *= -1
            self.velocity[1] = random.choice([-1, 1])
            
    def checkScreenBoundaries(self):
        if self.ball.getX() < -200:
            self.setDefaultValues()
            self.scores[1] += 1

        if self.ball.getX()+20 > self.WINDOW_WIDTH+200:
            self.setDefaultValues()
            self.scores[0] += 1

        if self.ball.getY() < 0 or self.ball.getY()+20 > self.WINDOW_HEIGHT:
            self.velocity[0] *= -1
            self.velocity[1] *= -1
    
    def endGame(self, score, player):
        self.SCREEN.fill('gray20')
        winner_surface = self.my_font.render('Winner: ' + player + ' SCORE:' + str(score), False, 'White')
        self.SCREEN.blit(winner_surface, (0, 0))
        pygame.display.update()
        pygame.time.wait(2000)
        self.scores[0] = 0
        self.scores[1] = 0        
        self.setDefaultValues()
    
    def setMainMenu(self):
        self.SCREEN.fill('gray20')
        
        start_surface = self.my_font.render(str('Start'), False, 'pink')
        self.SCREEN.blit(start_surface, (150, 150))
        settings_surface = self.my_font.render(str('Settings'), False, 'White')
        self.SCREEN.blit(settings_surface, (150, 200))
        quit_surface = self.my_font.render(str('Quit'), False, 'White')
        self.SCREEN.blit(quit_surface, (150, 250)) 

    # Main game loop
    def main(self):
        while True:
            self.SCREEN.fill('gray20')
            self.drawObjects()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.main_menu = False
                        self.start = True
                        self.begin_text = ' '
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu = True
            
            if self.start == True:
                self.defineKeyBindings()
                # Check if one of the players has won
                if self.scores[0] == 10:
                    self.endGame(self.scores[0], "Player 1")
                if self.scores[1] == 10:
                    self.endGame(self.scores[1], "Player 2")
                
                self.checkCollisions(ballRect, pad1Rect)
                self.checkCollisions(ballRect, pad2Rect)
                self.checkScreenBoundaries()

                self.ball.setX(self.ball.getX() + self.velocity[0])
                self.ball.setY(self.ball.getY() + self.velocity[1])
                
            elif self.main_menu:
                self.setMainMenu()
            self.CLOCK.tick(60)
            pygame.display.update()

if __name__ == '__main__':
    Game()
