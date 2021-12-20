#snake bitches

import pygame
from pygame.locals import *
import time
import random

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/weed.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = [pygame.image.load("resources/block.jpg").convert(), pygame.image.load("resources/block2.jpg").convert()]
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        

        self.parent_screen.blit(self.image[0], (self.x[0], self.y[0]))  #Head
        for i in range(1, self.length):
            self.parent_screen.blit(self.image[1], (self.x[i], self.y[i]))
        pygame.display.flip()
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("snake")
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.level = 1
        

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    
    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))


    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occured"
        
          # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound('crash')
            raise "Hit the boundry error"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length} Level: {self.level}",True,(255, 0, 127))
        
        self.surface.blit(score,(700,10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length} Level: {self.level}", True, (255, 0, 127))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("level 1, press '1'", True, (255, 0, 127))
        self.surface.blit(line2, (200, 350))
        line3 = font.render("level 2, press '2'", True, (255, 0, 127))
        self.surface.blit(line3, (200, 400))
        line4 = font.render("level 3, press '3'. To exit press Escape!", True, (255, 0, 127))
        self.surface.blit(line4, (200, 450))
        

        pygame.display.flip()

    

    def run(self):
        running = True
        pause = False
        speed = 0.15
        level = '1'
       

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        pause = False
                        speed = 0.15
                        self.level = '1'
                    if event.key == K_2:
                        pause = False
                        speed = 0.09
                        self.level = '2'
                    if event.key == K_3:
                        pause = False
                        speed = 0.05
                        self.level = "3"
                    if event.key == K_ESCAPE:
                        running = False

                    


                    

                    if not pause:
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
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(speed)

if __name__ == '__main__':
    game = Game()
    game.run()

