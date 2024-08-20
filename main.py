import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updateable, drawable)
  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = (updateable)
  Shot.containers = (shots, updateable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      
    pygame.Surface.fill(screen, (0,0,0))
    for obj in drawable:
      obj.draw(screen)

    for obj in updateable:
      obj.update(dt)

    for obj in asteroids:
      is_collided = obj.check_collision(player)

      for shot in shots:
        shot_asteroid = shot.check_collision(obj)
        if shot_asteroid:
          shot.kill()
          obj.split()

      if is_collided:
        exit("Game over!")
    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()