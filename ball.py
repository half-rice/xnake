import pygame
import random

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
    self.speed = random.randint(1,5)
    self.color = (random.randint(255,255),random.randint(0,0),random.randint(136,255))
    self.pos = (self.x,self.y)
    self.radius = 10

    balls.append(self)

  def getColor():
    return color

  def setColor(color):
    self.color = color

for i in range(200):
  makeBall() 

run = True 
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
      elif event.key == pygame.K_DOWN:
      elif event.key == pygame.K_LEFT:
      elif event.key == pygame.K_RIGHT:

    #if event.type == pygame.KEYUP:
    #  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #    x_change = 0
    #  if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #    y_change = 0

  for ball in balls:
    if ball.x >= 5 and ball.x <= screen_width-5:
      ball.x += ball.speed
    else:
      ball.x -+ ball.speed
    if ball.y >= 5 and ball.y <= screen_height-5:
      ball.y += ball.speed
    else:
      ball.y -= ball.speed


  gameDisplay.fill(black)

  for ball in balls:
    pygame.draw.circle(gameDisplay, ball.color, (ball.x,ball.y), ball.radius)
    #pygame.draw.circle(gameDisplay, red, (60,60), 10)

  pygame.display.update()
  clock.tick(15)



pygame.quit()
quit()