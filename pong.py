import pygame
import sys
from pygame.locals import *

class Game():

    def __init__(self):

        self.CLOCK = None
        self.SCREEN = None
        self.my_font = None

        self.BLACK = (0, 0, 0)
        self.WHITE = (200, 200, 200)
        self.WINDOW_HEIGHT = 420
        self.WINDOW_WIDTH = 420
        self.BLOCSIZE = 20 #Set the size of the grid block
        self.start = True

        self.x_pong1 = 20
        self.y_pong1 = 180
        self.x_pong2 = 380
        self.y_pong2 = 180
        self.x_ball_pos = 200
        self.y_ball_pos = 200
        self.x_velocity = 20
        self.y_velocity = 2
        self.score1 = 0
        self.score2 = 0

        self.main()
    
    def main(self):
        pygame.init()
        self.CLOCK = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.font.init()
        self.my_font = pygame.font.Font('Font/Pixeltype.ttf',50)

        while True:
            self.CLOCK.tick(60)
            self.SCREEN.fill(self.BLACK)
            self.objects()
            text_surface = self.my_font.render(str(self.score1) + ' :SCORE: ' + str(self.score2), False, 'White')
            self.SCREEN.blit(text_surface, (120, 0))

            self.endGame()
            
            self.controllers()
            
            self.collisions()
            
            self.checkScreenBoundaries()
            
            self.x_ball_pos += self.x_velocity
            self.y_ball_pos += self.y_velocity      
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    
    def objects(self):
        pygame.draw.rect(self.SCREEN, self.WHITE, (self.x_ball_pos, self.y_ball_pos, self.BLOCSIZE, self.BLOCSIZE))
        pygame.draw.rect(self.SCREEN, self.WHITE, (self.x_pong1, self.y_pong1, self.BLOCSIZE, self.BLOCSIZE*3))        
        pygame.draw.rect(self.SCREEN, self.WHITE, (self.x_pong2, self.y_pong2, self.BLOCSIZE, self.BLOCSIZE*3))

    def controllers(self):
        keys = pygame.key.get_pressed()   
        if keys[pygame.K_w] and self.y_pong1 > 0:
            self.y_pong1 -= 5
        if keys[pygame.K_s] and self.y_pong1 < self.WINDOW_HEIGHT - self.BLOCSIZE*3:
            self.y_pong1 += 5
        if keys[pygame.K_UP] and self.y_pong2 > 0:
            self.y_pong2 -= 5
        if keys[pygame.K_DOWN] and self.y_pong2 < self.WINDOW_HEIGHT - self.BLOCSIZE*3:
            self.y_pong2 += 5

    def collisions(self):
        # Ball and pad 1  
        if self.x_ball_pos-20 == self.x_pong1:    
            if self.y_ball_pos < self.y_pong1+(20*3):    
                if self.y_ball_pos+20 > self.y_pong1:
                    self.x_velocity *= -1          
        # Ball and pad 2      
        if self.x_ball_pos+20 == self.x_pong2:    
            if self.y_ball_pos+20 >  self.y_pong2:
                if self.y_ball_pos < self.y_pong2+(20*3):
                    self.x_velocity *= -1

    def checkScreenBoundaries(self):
        if self.x_ball_pos < 0:
                self.x_velocity *= -1
                self.y_velocity *= -1
                self.score2+=1
                
        if self.x_ball_pos+20 > self.WINDOW_WIDTH:    
            self.x_velocity *= -1
            self.y_velocity *= -1
            self.score1+=1
            
        if self.y_ball_pos < 0 or self.y_ball_pos+20 > self.WINDOW_HEIGHT:   
            self.x_velocity *= -1
            self.y_velocity *= -1

    def endGame(self):
        if self.score1 == 100:
            self.SCREEN.fill('Black')
            winner_surface = self.my_font.render('Winner: Player 1' + ' SCORE:' + str(self.score1), False, 'White')
            self.SCREEN.blit(winner_surface, (0, 0))
            pygame.display.update()
            pygame.time.wait(1000)
        
        if self.score2 == 100:
            self.SCREEN.fill('Black')
            winner_surface = self.my_font.render('Winner: Player 2' + ' SCORE:' + str(self.score2), False, 'White')
            self.SCREEN.blit(winner_surface, (0, 0))
            pygame.display.update()
            pygame.time.wait(1000)


game = Game()
