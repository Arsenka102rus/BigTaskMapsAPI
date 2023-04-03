import pygame
import sys
import map_pygame


#   Выключение игры
def terminate():
    pygame.quit()
    sys.exit()


map_pygame.main()
terminate()