import sys
import random
import pygame
from pygame.locals import QUIT,Rect,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN

pygame.init()
pygame.key.set_repeat(5,5)
surface = pygame.display.set_mode([600,600])
pygame.display.set_caption(('SNAKE_object'))
fps = pygame.time.Clock()

class Snake:
    def __init__(self,pos):
        self.bodies = [pos]

    def move(self,key):
        xpos,ypos = self.bodies[0]

        if key == K_LEFT:
            xpos -= 1
        elif key == K_RIGHT:
            xpos += 1
        elif key == K_UP:
            ypos -= 1
        elif ypos == K_DOWN:
            ypos += 1

        head = (xpos,ypos)

        is_game_over = head in self.bodies or \
                       head[0] < 0 or head[0] >= w or \
                       head[1] < 0 or head[1] >= h

        self.bodies.insert(0,head)

        if head in foods:
            i = foods.index(head)
            del foods[i]
            add_food(self)
        else:
            self.bodies.pop()

        return is_game_over

    def draw(self):
        for body in self.bodies:
            pygame.draw.rect(surface,(0,255,255),Rect(body[0]*30,body[1]*30,30,30))

foods = []
(w,h) = (20,20)

def add_food(snake):
    while True:
        pos = (random.randint(0,w-1),random.randint(0,h-1))
        if pos in foods or pos in snake.bodies:
            continue
        foods.append(pos)
        break

def paint(snake,message):
    surface.fill((0,0,0))
    snake.draw()
    for food in foods:
        pygame.draw.ellipse(surface,(0,255,0),Rect(food[0]*30,food[1]*30,30,30))

    for index in range(20):
        pygame.draw.line(surface,(64,64,64),(index*30,0),(index*30,600))
        pygame.draw.line(surface,(64,64,64),(0,index*30),(600,index*30))

    if message != None:
        surface.blit(message,(150,300))

    pygame.display.update()

def main():
    myfont = pygame.font.SysFont(None,80)
    key = K_DOWN
    message = None
    game_over = False
    snake = Snake((int(w/2),int(h/2)))

    for _ in range(10):
        add_food(snake)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                key = event.key

        if game_over:
            message = myfont.render('GAME OVER!',True,(255,0,0))
        else:
            game_over = snake.move(key)

        paint(snake,message)

        fps.tick(10)

if __name__ == '__main__':
    main()
    


