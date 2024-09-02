import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    running = True

    while running:
        # listen for window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)

        # render the game
        screen.fill("black")
        player.draw(screen)

        # refresh the screen
        pygame.display.flip()
        dt = clock.tick(120) / 1000
    pygame.quit()

if __name__ == "__main__":
    main()