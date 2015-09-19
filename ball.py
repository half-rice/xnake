import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('xnake')

x = 300
y = 300
x_change = 0
y_change = 0

clock = pygame.time.Clock()

balls = []
for i in range(50):
  makeBall() 

run = True 
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        y_change -= 10
        x_change = 0
      elif event.key == pygame.K_DOWN:
        y_change += 10
        x_change = 0
      elif event.key == pygame.K_LEFT:
        x_change = -10
        y_change = 0
      elif event.key == pygame.K_RIGHT:
        x_change = 10
        y_change = 0

    #if event.type == pygame.KEYUP:
    #  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #    x_change = 0
    #  if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #    y_change = 0

  if x_change >= 800 or x_change == 0 or y_change >= 600 or y_change == 0:
    x_change *= -1
    y_change *= -1


  x += x_change
  y += y_change

  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, black, [x,y,10,10])

  for ball in balls:
    pygame.draw.circle(gameDisplay, ball.color, ball.pos, ball.radius)
    #pygame.draw.circle(gameDisplay, red, (60,60), 10)

  pygame.display.update()
  clock.tick(15)

def makeBall():
  ball = Ball()
  return ball

class Ball(object):
  color = (0,0,0)
  pos = 0
  radius = 0

  def __init__(self):
    self.color = (randint(60,90),randint(100,140),randint(50,80))
    self.pos = (randint(0,800),(0,600))
    self.radius = 5

    balls.append(self)

  def getColor():
    return color

  def setColor(color):
    self.color = color

pygame.quit()
quit()