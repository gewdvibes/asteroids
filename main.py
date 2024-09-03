import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # adding objects to groups
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Making objects
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while running:
        # listen for window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update objects
        for updatables in updatable:
            updatables.update(dt)

        # check for collision
        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                running = False

        # render the game
        screen.fill("black")

        # render objects
        for drawables in drawable:
            drawables.draw(screen)

        # refresh the screen
        pygame.display.flip()
        dt = clock.tick(120) / 1000
    pygame.quit()
    print("Game over!")

if __name__ == "__main__":
    main()