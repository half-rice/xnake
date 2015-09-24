import pygame
import random
import makeBall

pygame.init()
screen_width = 1920/2
screen_height = 1080/2

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('xnake')

clock = pygame.time.Clock()

balls = []
def makeBall():
  ball = Ball()
  return ball

class Ball(object):
  color = (0,0,0)
  pos = 0
  radius = 0

  def __init__(self):
    self.x = screen_width/2
    self.y = screen_height/2
    self.x_speed = 1+random.randint(-8,6)
    self.y_speed = 1+random.randint(-8,6)
    self.color = (random.randint(255,255),random.randint(0,0),random.randint(136,255))
    self.pos = (self.x,self.y)
    self.radius = 10

    balls.append(self)

for i in range(500):
  makeBall() 

run = True 
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        a = null
      elif event.key == pygame.K_DOWN:
        a = null
      elif event.key == pygame.K_LEFT:
        a = null
      elif event.key == pygame.K_RIGHT:
        a = null

    #if event.type == pygame.KEYUP:
    #  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #    x_change = 0
    #  if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #    y_change = 0

  for ball in balls:

    if ball.x <= 5 or ball.x >= screen_width-5:
      ball.x_speed *= -1 
    if ball.y <= 5 or ball.y >= screen_height-5:
      ball.y_speed *= -1
    ball.x += ball.x_speed
    ball.y += ball.y_speed

  gameDisplay.fill(black)

  for ball in balls:
    pygame.draw.circle(gameDisplay, ball.color, (ball.x,ball.y), ball.radius)
    #pygame.draw.circle(gameDisplay, red, (60,60), 10)

  pygame.display.update()
  clock.tick(60)



pygame.quit()
quit()