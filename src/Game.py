import pygame
import sys
from pygame.locals import *
import random

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.startScreen()
        self.my_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
        self.WINDOW_HEIGHT = 420
        self.WINDOW_WIDTH = 420
        self.BLOCSIZE = 20  # Set the size of the grid block
        self.CLOCK = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        # Scores for player 1 and 2
        self.scores = [0, 0]
        self.main()
        # Testing

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = True
                        self.begin_text = ' '
            self.CLOCK.tick(60)
            self.SCREEN.fill('gray20')
            self.objects()
            if self.start == True:
                if self.scores[0] == 10:
                    self.endGame(self.scores[0], "Player 1")
                if self.scores[1] == 10:
                    self.endGame(self.scores[1], "Player 2")
                    
                self.controllers()
                self.collisions()
                self.checkScreenBoundaries()

                self.ball[0] += self.velocity[0]
                self.ball[1] += self.velocity[1]

            pygame.display.update()

    def objects(self):
        global ballRect, pad1Rect, pad2Rect
        ballRect = Rect(self.ball[0], self.ball[1],
                        self.BLOCSIZE, self.BLOCSIZE)
        pad1Rect = Rect(self.pad1[0], self.pad1[1], 10, self.BLOCSIZE*3)
        pad2Rect = Rect(self.pad2[0], self.pad2[1], 10, self.BLOCSIZE*3)

        pygame.draw.rect(self.SCREEN, 'mediumaquamarine', ballRect)
        pygame.draw.rect(self.SCREEN, 'maroon3', pad1Rect)
        pygame.draw.rect(self.SCREEN, 'maroon3', pad2Rect)

        score_surface = self.my_font.render(str(self.scores[0]) +
                     ' :SCORE: ' +
                      str(self.scores[1]), False, 'White')
                      
        self.SCREEN.blit(score_surface, (120, 0))
            
        begin_surface = self.my_font.render(str(self.begin_text), False, 'White')
        self.SCREEN.blit(begin_surface, (60, 120)) 

    def controllers(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pad1[1] > 0:
            self.pad1[1] -= 5
        if keys[pygame.K_s] and self.pad1[1] < self.WINDOW_HEIGHT - self.BLOCSIZE*3:
            self.pad1[1] += 5
        if keys[pygame.K_UP] and self.pad2[1] > 0:
            self.pad2[1] -= 5
        if keys[pygame.K_DOWN] and self.pad2[1] < self.WINDOW_HEIGHT - self.BLOCSIZE*3:
            self.pad2[1] += 5

    def collisions(self):
        # Ball and pad 1 in X
        if ballRect.colliderect(pad1Rect):
            self.velocity[0] *= -1
            self.velocity[1] = random.choice([-1, 1])
        # Ball and pad 2 in X
        if ballRect.colliderect(pad2Rect):
            self.velocity[0] *= -1
            self.velocity[1] = random.choice([-1, 1])

    def checkScreenBoundaries(self):
        if self.ball[0] < -200:
            self.startScreen()
            self.scores[1] += 1

        if self.ball[0]+20 > self.WINDOW_WIDTH+200:
            self.startScreen()
            self.scores[0] += 1  

        if self.ball[1] < 0 or self.ball[1]+20 > self.WINDOW_HEIGHT:
            self.velocity[0] *= -1
            self.velocity[1] *= -1

    def endGame(self, score, player):
        self.SCREEN.fill('gray20')
        winner_surface = self.my_font.render(
            'Winner: ' + player + ' SCORE:' + str(score), False, 'White')
        self.SCREEN.blit(winner_surface, (0, 0))
        pygame.display.update()
        pygame.time.wait(2000)
        self.scores[0] = 0
        self.scores[1] = 0
        self.startScreen()
    
    # Initialize the game main variables
    def startScreen(self):
        self.start = False
        self.pad1 = [0, 180]
        self.pad2 = [410, 180]
        self.ball = [200, 200]
        self.velocity = [10, 1]
        self.begin_text = 'Press SPACE to start'

game = Game()
