import pygame
import time
pygame.init ()
width = 1000
height = 800
gameDisplay = pygame.display.set_mode ( ( width , height ) )
pygame.display.set_caption ( 'Game Ball' )
clock = pygame.time.Clock ()
def game_loop () :
  for event in pygame.event.get () :
    if event.type == pygame.QUIT () :
      pygame.quit ()
      quit ()
