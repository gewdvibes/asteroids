import pygame
import asteroid as a
import asteroidfield as af
import constants as c
import player as p
import shot as s

def main():
    print("Starting asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # adding objects to groups
    p.Player.containers = (drawable, updatable)
    a.Asteroid.containers = (asteroids, drawable, updatable)
    af.AsteroidField.containers = (updatable)
    s.Shot.containers = (shots, drawable, updatable)

    # Making objects
    player = p.Player((c.SCREEN_WIDTH / 2), (c.SCREEN_HEIGHT / 2), c.PLAYER_RADIUS)
    asteroid_field = af.AsteroidField()

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

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_detection(shot):
                    asteroid.split()
                    shot.kill()

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
