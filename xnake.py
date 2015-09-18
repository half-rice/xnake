import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('xnake')

pygame.display.update()

run = True 
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False;
    #print(event)

pygame.quit()
quit()