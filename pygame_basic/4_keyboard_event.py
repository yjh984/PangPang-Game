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
to_x = 0
to_y = 0
move_step = 0.2
key_left_pressed = False
key_right_pressed = False
key_up_pressed = False
key_down_pressued = False

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                to_x = -move_step
                key_left_pressed = True
            if e.key == pygame.K_RIGHT:
                to_x = move_step
                key_right_pressed = True
            if e.key == pygame.K_UP:
                to_y = -move_step
                key_up_pressed = True
            if e.key == pygame.K_DOWN:
                to_y = move_step
                key_down_pressued = True
            # print(e.key)
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                key_left_pressed=False
                if key_right_pressed==False: to_x=0
                else: to_x=move_step
            if e.key == pygame.K_RIGHT:
                key_right_pressed=False
                if key_left_pressed==False: to_x=0
                else: to_x=-move_step
            if e.key == pygame.K_UP:
                key_up_pressed=False
                if key_down_pressued==False: to_y=0
                else: to_y=move_step
            if e.key == pygame.K_DOWN:
                key_down_pressued=False
                if key_up_pressed==False: to_y=0
                else: to_y=-move_step

    # print(to_x)
    chart_x_pos += to_x
    chart_y_pos += to_y
    if chart_x_pos<0: chart_x_pos=0
    if chart_x_pos>screen_width-chart_width: chart_x_pos=screen_width-chart_width
    if chart_y_pos<0: chart_y_pos=0
    if chart_y_pos>screen_height-chart_height: chart_y_pos=screen_height-chart_height

    # screen.fill((0,0,255))
    screen.blit(background,(0,0))
    screen.blit(chart,(chart_x_pos, chart_y_pos))
    pygame.display.update()

    # to_x=0
    # to_y=0


pygame.quit()