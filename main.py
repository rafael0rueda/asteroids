# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateble, drawable)
    # Player have to go below the containers
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateble.update(dt)
        
        screen.fill((0,0,0)) 
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        # Limit the frame to 60 FPS
        dt = time.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()
