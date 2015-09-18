import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('xnake')

rx = 300
ry = 300
xspeed = 0
yspeed = 0

clock = pygame.time.Clock()

run = True 
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        yspeed -= 10
      if event.key == pygame.K_DOWN:
        yspeed += 10
      if event.key == pygame.K_LEFT:
        xspeed = -10
      if event.key == pygame.K_RIGHT:
        xspeed = 10

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        xspeed = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        yspeed = 0

  rx += xspeed
  ry += yspeed

  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, black, [rx,ry,10,10])

  pygame.display.update()
  clock.tick(15)

pygame.quit()
quit()