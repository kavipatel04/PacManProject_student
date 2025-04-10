import pygame
import sys
from pacman import Pacman
from ghost import Ghost
from game_board import GameBoard

# Initialize Pygame
pygame.init()

# Game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
GHOST_COLORS = [(255, 0, 0), (255, 182, 255), (0, 255, 255), (255, 182, 85)]

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Create game objects
game_board = GameBoard()
pacman = Pacman(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
ghosts = [
    Ghost(100, 100, GHOST_COLORS[0]),
    Ghost(WINDOW_WIDTH - 100, 100, GHOST_COLORS[1]),
    Ghost(100, WINDOW_HEIGHT - 100, GHOST_COLORS[2]),
    Ghost(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100, GHOST_COLORS[3]),
]
score = 0
game_over = False


def check_collisions():
    global score, game_over

    # Check pellet collisions
    for pellet in game_board.pellets:
        if (
            not pellet.collected
            and abs(pellet.x - pacman.x) < 15
            and abs(pellet.y - pacman.y) < 15
        ):
            pellet.collected = True
            score += 10

    # Check power pellet collisions
    for power_pellet in game_board.power_pellets:
        if (
            not power_pellet.collected
            and abs(power_pellet.x - pacman.x) < 15
            and abs(power_pellet.y - pacman.y) < 15
        ):
            power_pellet.collected = True
            score += 50
            # Make ghosts scared
            for ghost in ghosts:
                ghost.scared = True
                ghost.scared_timer = 300  # 5 seconds at 60 FPS

    # Check ghost collisions
    for ghost in ghosts:
        if abs(ghost.x - pacman.x) < 20 and abs(ghost.y - pacman.y) < 20:
            if ghost.scared:
                ghost.x = WINDOW_WIDTH // 2
                ghost.y = WINDOW_HEIGHT // 2
                score += 200
            else:
                game_over = True


def main():
    global game_over
    score = 0
    while True:
        # Handle events
        # score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    # Reset game
                    game_over = False
                    pacman.x = WINDOW_WIDTH // 2
                    pacman.y = WINDOW_HEIGHT // 2
                    for ghost in ghosts:
                        ghost.scared = False
                    score = 0

        if not game_over:
            # Handle pacman movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                pacman.move("right", game_board.walls)
            elif keys[pygame.K_LEFT]:
                pacman.move("left", game_board.walls)
            elif keys[pygame.K_UP]:
                pacman.move("up", game_board.walls)
            elif keys[pygame.K_DOWN]:
                pacman.move("down", game_board.walls)

            # Move ghosts
            for ghost in ghosts:
                ghost.move(game_board.walls, pacman)

            # Check collisions
            check_collisions()

        # Draw everything
        screen.fill(BLACK)
        game_board.draw(screen)
        pacman.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)

        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render(
                "Game Over! Press R to restart", True, (255, 255, 255)
            )
            screen.blit(game_over_text, (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
