# TODO: Rust webassembly?
import pygame

class Body(object):
    def __init__(self):
        pass

class Actor(object):
    def __init__(self):
        self.position = 0
        self.velocity = 0

    def tick(self, dt):
        self.position += self.velocity 

class World(object):
    def __init__(self):
        self.player = Actor()
    
    def tick(self, dt):
        self.player.tick(dt)

def render(screen, world, background):
    screen.fill(background)
    pygame.draw.circle(screen, (20, 220, 42), (320, 210), 146)
    pygame.draw.rect(screen, (255,127,80), (320 - 4, 210 - 146 - 20, 8, 20))
    pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 420))
    pygame.display.set_caption("Little Planet")
    running = True
    background = (255, 255, 0)

    world = World()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.uo
                elif event.key == pygame.K_d:
                    pass

            world.tick(1.0 / 30)
            render(screen, world, background)

if __name__ == "__main__":
    main()