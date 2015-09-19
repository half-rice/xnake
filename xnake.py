import pygame
import time
import random

pygame.init()

display_width = 1920/2
display_height = 1080/2
fps = 30
block = 10
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('xnake')

def msg(msg, color):
  screen_text = font.render(msg, True, color)
  gameDisplay.blit(screen_text, [display_width/2,display_height/2])

def game():
  gameExit = 0
  gameOver = 0

  # set reticle attributes
  x = display_width/2
  y = display_height/2
  x_change = 0
  y_change = 0

  while not gameExit:
    while gameOver == 1:
      gameDisplay.fill(white)
      msg("Loser, press c to play again, q to quit", red)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameExit = 1
            gameOver = 0
          if event.key == pygame.K_c:
            game()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameExit = 1;

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          y_change = -block
          x_change = 0
        elif event.key == pygame.K_DOWN:
          y_change = block
          x_change = 0
        elif event.key == pygame.K_LEFT:
          x_change = -block
          y_change = 0
        elif event.key == pygame.K_RIGHT:
          x_change = block
          y_change = 0

    if x >= display_width or x < 0 or y >= display_height or y < 0:
      gameOver = 1;

    x += x_change
    y += y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [x,y,10,10])

    pygame.display.update()
    clock.tick(fps)

  pygame.quit()
  quit()

game()