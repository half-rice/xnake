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

  if x_change >= 800 or x_change = 0 or y_change >= 600 or y_change = 0:


  x += x_change
  y += y_change

  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, black, [rx,ry,10,10])

  pygame.display.update()
  clock.tick(15)

pygame.quit()
quit()