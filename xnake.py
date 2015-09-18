import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('xnake')

lead_x = 300
lead_y = 300

run = True 
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        lead_y -= 10
      if event.key == pygame.K_DOWN:
        lead_y += 10
      if event.key == pygame.K_LEFT:
        lead_x -= 10
      if event.key == pygame.K_RIGHT:
        lead_x += 10



  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])

  gameDisplay.fill(red, rect=[200,200,50,50])

  pygame.display.update()

pygame.quit()
quit()