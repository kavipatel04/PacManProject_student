import pygame


class Pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 2
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)


class PowerPellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
