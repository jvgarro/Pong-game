from tarfile import BLOCKSIZE
from turtle import width
import pygame
import sys
import random
from pygame.locals import *
from pyparsing import White

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 420
WINDOW_WIDTH = 420
BLOCSIZE = 20 #Set the size of the grid block
start = True

def main():
    global SCREEN, CLOCK, x_ball_pos, y_ball_pos, x_velocity, y_velocity, x_pong1, y_pong1, x_pong2, y_pong2
    x_pong1 = 20
    y_pong1 = 180
    x_pong2 = 380
    y_pong2 = 180
    x_ball_pos = 200
    y_ball_pos = 200
    x_velocity = 5
    y_velocity = 1
    score1 = 0
    score2 = 0
    pygame.init()
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.font.init()
    my_font = pygame.font.Font('Font/Pixeltype.ttf',50)

    while True:
        CLOCK.tick(60)
        SCREEN.fill(BLACK)
        objects()
        text_surface = my_font.render(str(score1) + ' :SCORE: ' + str(score2), False, WHITE)
        SCREEN.blit(text_surface, (120, 0))
        
        # Controllers
        keys = pygame.key.get_pressed()   
        if keys[pygame.K_w] and y_pong1 > 0:
            y_pong1 -= 5
        if keys[pygame.K_s] and y_pong1 < WINDOW_HEIGHT - BLOCSIZE*3:
            y_pong1 += 5
        if keys[pygame.K_UP] and y_pong2 > 0:
            y_pong2 -= 5
        if keys[pygame.K_DOWN] and y_pong2 < WINDOW_HEIGHT - BLOCSIZE*3:
            y_pong2 += 5
        
        # Collisions:
        # Ball and pad 1  
        if x_ball_pos-20 == x_pong1:    
            if y_ball_pos < y_pong1+(20*3):    
                if y_ball_pos+20 > y_pong1:
                    x_velocity *= -1          
        # Ball and pad 2      
        if x_ball_pos+20 == x_pong2:    
            if y_ball_pos+20 >  y_pong2:
                if y_ball_pos < y_pong2+(20*3):
                    x_velocity *= -1
        
        # Screen boundaries
        if x_ball_pos < 0:
            x_velocity *= -1
            y_velocity *= -1
            score2+=1
            
        if x_ball_pos+20 > WINDOW_WIDTH:    
            x_velocity *= -1
            y_velocity *= -1
            score1+=1
        
        if y_ball_pos < 0 or y_ball_pos+20 > WINDOW_HEIGHT:   
            x_velocity *= -1
            y_velocity *= -1
        
        x_ball_pos += x_velocity
        y_ball_pos += y_velocity      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
            
# Game objects
def objects():
    pygame.draw.rect(SCREEN, WHITE, (x_ball_pos, y_ball_pos, BLOCSIZE, BLOCSIZE))
    pygame.draw.rect(SCREEN, WHITE, (x_pong1, y_pong1, BLOCSIZE, BLOCSIZE*3))        
    pygame.draw.rect(SCREEN, WHITE, (x_pong2, y_pong2, BLOCSIZE, BLOCSIZE*3))
            
if __name__ == '__main__':
    main()