import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Soccer Game")

# Colors
GREEN = (50, 150, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

# Game Objects
ball_radius = 25
ball_pos = [100, 100]
ball_dragging = False

goal_rect = pygame.Rect(WIDTH - 120, HEIGHT // 2 - 60, 100, 120)

score = 0
game_over = False

clock = pygame.time.Clock()

def draw_ball():
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

def draw_goal():
    pygame.draw.rect(screen, YELLOW, goal_rect)

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

def draw_victory():
    text = font.render("🎉 Victory!", True, WHITE)
    restart = small_font.render("Click to Play Again", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 40))
    screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2 + 20))

def reset_game():
    global score, game_over, ball_pos
    score = 0
    game_over = False
    ball_pos = [100, 100]

def is_ball_in_goal():
    ball_rect = pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius,
                            ball_radius * 2, ball_radius * 2)
    return goal_rect.colliderect(ball_rect)

# Main loop
running = True
while running:
    screen.fill(GREEN)
    draw_goal()
    draw_ball()
    draw_score()

    if game_over:
        draw_victory()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse press
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                reset_game()
            elif (ball_pos[0] - event.pos[0]) ** 2 + (ball_pos[1] - event.pos[1]) ** 2 < ball_radius ** 2:
                ball_dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            ball_dragging = False

        elif event.type == pygame.MOUSEMOTION and ball_dragging:
            ball_pos = list(event.pos)

    if not game_over and is_ball_in_goal():
        score += 1
        ball_pos = [100, 100]
        if score >= 5:
            game_over = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
