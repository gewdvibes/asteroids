import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        # listen for window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # render the game
        screen.fill("black")

        # refresh the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        player.draw(screen)

    pygame.quit()

if __name__ == "__main__":
    main()