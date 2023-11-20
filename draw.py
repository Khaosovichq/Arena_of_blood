import pygame

from constant import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, SKYBLUE, SKYGREEN

bg_image = pygame.image.load("assets/images/background/background.jpg")

def draw_text(text, font, text_col, screen, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def draw_bg(screen):
  scaled_bg = pygame.transform.scale(bg_image.convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health, screen, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, SKYBLUE, (x, y, 400, 30))
  pygame.draw.rect(screen, SKYGREEN, (x, y, 400 * ratio, 30))