import pygame
from item import PowerPellet, Pellet


class GameBoard:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.walls = []
        self.pellets = []
        self.power_pellets = []
        self.setup_maze()

    def setup_maze(self):
        # Create walls for a simple maze
        # Outer walls
        self.walls.extend(
            [
                pygame.Rect(0, 0, self.width, 20),  # Top
                pygame.Rect(0, 0, 20, self.height),  # Left
                pygame.Rect(0, self.height - 20, self.width, 20),  # Bottom
                pygame.Rect(self.width - 20, 0, 20, self.height),  # Right
            ]
        )

        # Inner walls
        self.walls.extend(
            [
                pygame.Rect(100, 100, 20, 200),
                pygame.Rect(300, 100, 200, 20),
                pygame.Rect(600, 100, 20, 400),
                pygame.Rect(300, 350, 200, 20),
            ]
        )

        # Add pellets
        for x in range(40, self.width - 40, 40):
            for y in range(40, self.height - 40, 40):
                # Check if pellet position conflicts with walls
                can_place = True
                for wall in self.walls:
                    if wall.collidepoint(x, y):
                        can_place = False
                        break

                if can_place:
                    self.pellets.append(Pellet(x, y))

        # Add power pellets in corners
        power_pellet_positions = [
            (50, 50),
            (self.width - 50, 50),
            (50, self.height - 50),
            (self.width - 50, self.height - 50),
        ]

        for pos in power_pellet_positions:
            self.power_pellets.append(PowerPellet(pos[0], pos[1]))

    def draw(self, screen):
        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, (0, 0, 255), wall)

        # Draw pellets and power pellets
        for pellet in self.pellets:
            pellet.draw(screen)
        for power_pellet in self.power_pellets:
            power_pellet.draw(screen)
