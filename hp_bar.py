def draw_health_bar(health, screen, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, SKYBLUE, (x, y, 400, 30))
  pygame.draw.rect(screen, SKYGREEN, (x, y, 400 * ratio, 30))