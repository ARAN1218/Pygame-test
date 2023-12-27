import sys
import math
import random
import pygame
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,Rect

class Block:
    def __init__(self,col,rect,speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45,45) + 270

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(surface,self.col,self.rect)
        else:
            pygame.draw.ellipse(surface,self.col,self.rect)

def tick():
    global BLOCKS

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                paddle.rect.centerx -= 10
            elif event.key == K_RIGHT:
                paddle.rect.centerx += 10

    if ball.rect.centery < 1000:
        ball.move()

    prevlen = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS
              if not x.rect.colliderect(ball.rect)]
    
    if len(BLOCKS) != prevlen:
        ball.dir *= -1

    if paddle.rect.colliderect(ball.rect):
        ball.dir = 90 + (paddle.rect.centerx - ball.rect.centerx) / paddle.rect.width * 80

    if ball.rect.centerx < 0 or ball.rect.centerx > 600:
        ball.dir = 180 - ball.dir
    if ball.rect.centery < 0:
        ball.dir = -ball.dir
        ball.speed = 15

pygame.init()
pygame.key.set_repeat(5,5)
surface = pygame.display.set_mode((600,800))
pygame.display.set_caption(('BLOCK'))
fpsclock = pygame.time.Clock()

BLOCKS = []
paddle = Block((242,242,0),Rect(300,700,100,30))
ball = Block((242,242,0),Rect(300,400,20,20),10)

def main():
    myfont = pygame.font.SysFont(None,80)
    mess_clear = myfont.render('CLEARED!',True,(255,255,0))
    mess_over = myfont.render('GAME OVER!',True,(255,255,0))
    fps = 30
    colors = [(255,0,0),(255,165,0),(242,242,0),(0,128,0),(128,0,128),(0,0,250)]

    for ypos,color in enumerate(colors,start=0):
        for xpos in range(0,5):
            BLOCKS.append(Block(color,Rect(xpos*100 + 60,ypos*50 +40,80,30)))

    while True:
        tick()
        surface.fill((0,0,0))

        ball.draw()
        paddle.draw()

        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            surface.blit(mess_clear,(200,400))
        if ball.rect.centery > 800 and len(BLOCKS) > 0:
            surface.blit(mess_over,(150,400))

        pygame.display.update()
        fpsclock.tick(fps)

if __name__ == '__main__':
    main()
        


    
