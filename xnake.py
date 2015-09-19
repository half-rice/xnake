import pygame

pygame.init()

display_width = 1920/2
display_height = 1080/2
fps = 30
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

x = display_width/2
y = display_height/2
x_change = 0
y_change = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('xnake')

run = 1
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = 0;

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        y_change = -10
        x_change = 0
      elif event.key == pygame.K_DOWN:
        y_change = 10
        x_change = 0
      elif event.key == pygame.K_LEFT:
        x_change = -10
        y_change = 0
      elif event.key == pygame.K_RIGHT:
        x_change = 10
        y_change = 0

  if x >= display_width or x < 0 or y >= display_height or y_change < 0:
    print "oub"


  x += x_change
  y += y_change

  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, black, [x,y,10,10])

  pygame.display.update()
  clock.tick(fps)

pygame.quit()
quit()