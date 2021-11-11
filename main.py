import pygame
from pygame.locals import *
import time
import random

size = 40

class Apple:
    def __init__(self, parent_screen ):
        
        self.parent_screen = parent_screen
        self.image = pygame.image.load("C:/Users/31629/Documents/school/snake/apple.jpg").convert()
        self.x =  120
        self.y =  120

    def draw(self):
        
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()
    
    def move(self):
    
        self.x=random.randint(0,25)*size
        self.y=random.randint(0, 20)*size

class Snake:
    def __init__(self, parent_screen, lenght):
        self.length = lenght
        self.parent_screen = parent_screen
        self.head = pygame.image.load("C:/Users/31629/Documents/school/snake/head.jpg").convert()
        self.x = [40]*lenght
        self.y = [40]*lenght
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((255,233, 84))
        for i in range(self.length):
            self.parent_screen.blit(self.head,(self.x[i], self.y[i]))
        pygame.display.flip()
    
    def move_left(self):
        self.direction = 'left'

    def move_right(self):    
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'
    
    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
            
        self.draw()



class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 1000))
        # self.surface.fill((255,233, 84))
        self.snake = Snake(self.surface, 6)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.is_collision(self.snake.x[0], self.snake.x[0], self.apple.x, self.apple.x):
            self.apple.move()


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                      
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()
                      
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    
                      
                elif event.type == QUIT:
                    running = False
            
            self.play()
            time.sleep(0.3)                        
        
            
    

 
if __name__ == "__main__":
   game = Game()
   game.run()
   

   