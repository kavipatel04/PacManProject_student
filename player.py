# player.py
import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "right"
        self.speed = 2
        self.radius = 10
        self.mouth_angle = 45
        self.mouth_change = 5
        self.opening_mouth = True

    def move(self, direction, walls):
        new_x = self.x
        new_y = self.y

        if direction == "right":
            new_x += self.speed
        elif direction == "left":
            new_x -= self.speed
        elif direction == "up":
            new_y -= self.speed
        elif direction == "down":
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
                break

        if can_move:
            self.x = new_x
            self.y = new_y
            self.direction = direction

    def draw(self, screen):
        # Animate mouth
        if self.opening_mouth:
            self.mouth_angle += self.mouth_change
            if self.mouth_angle >= 45:
                self.opening_mouth = False
        else:
            self.mouth_angle -= self.mouth_change
            if self.mouth_angle <= 5:
                self.opening_mouth = True

        # Draw Pac-Man
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)

        # Draw mouth based on direction
        if self.direction == "right":
            start_angle = self.mouth_angle
            end_angle = 360 - self.mouth_angle
        elif self.direction == "left":
            start_angle = 180 + self.mouth_angle
            end_angle = 180 - self.mouth_angle
        elif self.direction == "up":
            start_angle = 270 + self.mouth_angle
            end_angle = 270 - self.mouth_angle
        else:  # down
            start_angle = 90 + self.mouth_angle
            end_angle = 90 - self.mouth_angle

        pygame.draw.arc(
            screen,
            (0, 0, 0),
            (
                self.x - self.radius,
                self.y - self.radius,
                self.radius * 2,
                self.radius * 2,
            ),
            start_angle * 3.14 / 180,
            end_angle * 3.14 / 180,
            3,
        )
