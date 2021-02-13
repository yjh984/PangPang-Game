import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Bubbles")
background = pygame.image.load("D:\\python-ws\\Bubbles\\pygame_basic\\scr\\background.png")

chart = pygame.image.load("D:\\python-ws\\Bubbles\\pygame_basic\\scr\\chart.png")
chart_size = chart.get_rect().size
chart_width = chart_size[0]
chart_height = chart_size[1]
chart_x_pos = (screen_width-chart_width)/2
chart_y_pos = screen_height-chart_height


#이벤트 루프
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    # screen.fill((0,0,255))
    screen.blit(background,(0,0))
    screen.blit(chart,(chart_x_pos, chart_y_pos))
    pygame.display.update()

pygame.quit()