import pygame

# game 초기화

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Bubbles")
background = pygame.image.load("D:\\python-ws\\Bubbles\\pygame_basic\\scr\\background.png")
clock=pygame.time.Clock()

# 캐랙터 및 적들 이미지 만들기, 텍스트 추가


#이벤트 루프
to_x = 0
to_y = 0
move_step = 0.4

running = True
while running:
    dt=clock.tick(60)

    # 이벤트 처리
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # 움직임 처리
    
    #collision

    # timer
    
    # screen.blit 처리
    
    pygame.display.update()


pygame.quit()