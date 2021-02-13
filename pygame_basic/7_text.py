import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Bubbles")
background = pygame.image.load("D:\\python-ws\\Bubbles\\pygame_basic\\scr\\background.png")
clock=pygame.time.Clock()

chart = pygame.image.load("D:\\python-ws\\Bubbles\\pygame_basic\\scr\\chart.png")
chart_size = chart.get_rect().size
chart_width = chart_size[0]
chart_height = chart_size[1]
chart_x_pos = (screen_width-chart_width)/2
chart_y_pos = screen_height-chart_height
chart_rect=chart.get_rect()

enemy = pygame.image.load("D:\\python-ws\\Bubbles\\pygame_basic\\scr\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width-enemy_width)/2
enemy_y_pos = (screen_height-enemy_height)/2
enemy_rect=enemy.get_rect()

#text입력
game_font=pygame.font.Font(None,20)
total_time=10
start_ticks=pygame.time.get_ticks()


#이벤트 루프
to_x = 0
to_y = 0
move_step = 0.4

key_left_pressed = False
key_right_pressed = False
key_up_pressed = False
key_down_pressued = False

running = True
while running:
    dt=clock.tick(60)

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
    chart_x_pos += to_x*dt
    chart_y_pos += to_y*dt
    if chart_x_pos<0: chart_x_pos=0
    if chart_x_pos>screen_width-chart_width: chart_x_pos=screen_width-chart_width
    if chart_y_pos<0: chart_y_pos=0
    if chart_y_pos>screen_height-chart_height: chart_y_pos=screen_height-chart_height

    #collision
    chart_rect.left=chart_x_pos
    chart_rect.top=chart_y_pos
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    if chart_rect.colliderect(enemy_rect):
        running=False

    # timer
    timer=game_font.render(str(int(total_time-(pygame.time.get_ticks()-start_ticks)/1000)),\
     True, (255,255,255))
    # screen.fill((0,0,255))
    screen.blit(background,(0,0))
    screen.blit(chart,(chart_x_pos, chart_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))
    screen.blit(timer,(10,10))
    pygame.display.update()

    # to_x=0
    # to_y=0

pygame.time.delay(500)
pygame.quit()