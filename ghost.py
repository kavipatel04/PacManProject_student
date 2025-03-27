import pygame
import random


class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 1
        self.radius = 10
        self.direction = random.choice(["right", "left", "up", "down"])
        self.scared = False
        self.scared_timer = 0

    def move(self, walls, player):
        if not self.scared:
            # Simple ghost AI: Try to move towards player with random variation
            if random.random() < 0.1:
                self.direction = random.choice(["right", "left", "up", "down"])
            else:
                # Move towards player
                if abs(player.x - self.x) > abs(player.y - self.y):
                    self.direction = "right" if player.x > self.x else "left"
                else:
                    self.direction = "down" if player.y > self.y else "up"

        new_x = self.x
        new_y = self.y

        if self.direction == "right":
            new_x += self.speed
        elif self.direction == "left":
            new_x -= self.speed
        elif self.direction == "up":
            new_y -= self.speed
        elif self.direction == "down":
            new_y += self.speed

        # Check collision with walls
        can_move = True
        for wall in walls:
            if pygame.Rect(
                new_x - self.radius,
                new_y - self.radius,
                self.radius * 2,
                self.radius * 2,
            ).colliderect(wall):
                can_move = False
                self.direction = random.choice(["right", "left", "up", "down"])
                break

        if can_move:
            self.x = new_x
            self.y = new_y

        if self.scared:
            self.scared_timer -= 1
            if self.scared_timer <= 0:
                self.scared = False

    def draw(self, screen):
        color = (0, 0, 255) if self.scared else self.color

        # Draw ghost body
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        pygame.draw.rect(
            screen, color, (self.x - self.radius, self.y, self.radius * 2, self.radius)
        )

        # Draw ghost eyes
        eye_color = (255, 255, 255) if not self.scared else (0, 0, 255)
        pygame.draw.circle(screen, eye_color, (self.x - 4, self.y - 2), 3)
        pygame.draw.circle(screen, eye_color, (self.x + 4, self.y - 2), 3)
