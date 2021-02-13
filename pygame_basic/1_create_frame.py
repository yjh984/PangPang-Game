import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Bubbles")

#이벤트 루프
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()