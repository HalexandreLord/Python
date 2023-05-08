import random
import pygame
from pygame.locals import *
from pygame import mixer



def on_grid_random():
   x = random.randint(0,590)
   y = random.randint(0,590)
   return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
   return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
#icon = pygame.image.load('pacman.png') #icone da janela
#pygame.display.set_icon(icon)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cobrinha by Halexandre Lord') #texto da janela

mixer.init() #modulo de som
som1 = pygame.mixer.Sound('morri.mp3') #som de ponto
som2 = pygame.mixer.Sound('errou.mp3') #som do gameover
mixer.music.set_volume(0.7)

snake = [(200,200), (210,200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

while True:
   clock.tick(20)
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()

       if event.type ==KEYDOWN:
           if event.key == K_UP:
               my_direction = UP
           if event.key == K_DOWN:
               my_direction = DOWN
           if event.key == K_LEFT:
               my_direction = LEFT
           if event.key == K_RIGHT:
               my_direction = RIGHT

   if collision(snake[0], apple_pos):
       apple_pos = on_grid_random()
       snake.append((0,0))
       score = score + 1
       som1.play()

   for i in range(len(snake) - 1, 0, -1):
       snake[i] = (snake[i - 1][0], snake[i - 1][1])

   #se a cobra colidir com a borda
   if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
       som2.play()
       game_over = True
       break

   if my_direction == UP:
       snake[0] = (snake[0][0], snake[0][1] -10)
   if my_direction == DOWN:
       snake[0] = (snake[0][0], snake[0][1] +10)
   if my_direction == RIGHT:
       snake[0] = (snake[0][0] +10, snake[0][1])
   if my_direction == LEFT:
       snake[0] = (snake[0][0] -10, snake[0][1])

   screen.fill((0,0,0))
   screen.blit(apple, apple_pos)

  #quadriculação para melhor visualização do jogo.
   #for x in range(0, 600, 10):  # Draw vertical lines
   #    pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
   #for y in range(0, 600, 10):  # Draw vertical lines
   #    pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

   #istema de pontuação
   score_font = font.render('Pontos: %s' % (score), True, (255, 255, 255))
   score_rect = score_font.get_rect()
   score_rect.topleft = (600 - 120, 10)
   screen.blit(score_font, score_rect)


   for pos in snake:
       screen.blit(snake_skin,pos)
   pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Fim de jogo', True, (255, 0, 0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 600 / 2)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
         for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                exit()

