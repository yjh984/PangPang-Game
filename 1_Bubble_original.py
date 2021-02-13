import pygame
import os

# game 초기화

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Nado Pang")
clock=pygame.time.Clock()

# background, stage 추가
current_path=os.path.dirname(__file__) #file이 있는 현재 dir 반환
image_path=os.path.join(current_path,'images')

background=pygame.image.load(os.path.join(image_path, 'background.png'))
stage=pygame.image.load(os.path.join(image_path,'stage.png'))
stage_size=stage.get_rect().size
stage_height=stage_size[1]

# 캐랙터 및 적들 이미지 만들기, 텍스트 추가
char=pygame.image.load(os.path.join(image_path,'character.png'))
char_size=char.get_rect().size
char_width=char_size[0]
char_height=char_size[1]
char_x_pos = (screen_width-char_width)/2
char_y_pos = screen_height-stage_height-char_height
char_to_x = 0
char_speed = 0.4

#무기 만들기
weapons=[]
weapon=pygame.image.load(os.path.join(image_path,'weapon.png'))
weapon_size=weapon.get_rect().size
weapon_width=weapon_size[0]
weapon_height=weapon_size[1]
weapon_speed=15

#공 만들기
ball_images=[
    pygame.image.load(os.path.join(image_path,'balloon1.png')),
    pygame.image.load(os.path.join(image_path,'balloon2.png')),
    pygame.image.load(os.path.join(image_path,'balloon3.png')),
    pygame.image.load(os.path.join(image_path,'balloon4.png'))
]
ball_speeds=[-18, -15, -12, -9]
balls=[]
balls.append({
    "pos_x": 50,
    "pos_y": 50,
    "img_idx": 0,
    "to_x": 3,
    "to_y": -6,
    "init_speed":ball_speeds[0]
})

#공, 무기 삭제
ball_remove = -1
weapon_remove = -1

# font 정의
game_font=pygame.font.Font(None, 40)
game_time=100
start_ticks=pygame.time.get_ticks()

game_result = "Game Over!!"

#이벤트 루프
key_left_pressed = False
key_right_pressed = False

running = True
while running:
    dt=clock.tick(30)

    # 이벤트 처리
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                char_to_x = -char_speed
                key_left_pressed = True
            if e.key == pygame.K_RIGHT:
                char_to_x = char_speed
                key_right_pressed = True
            if e.key== pygame.K_SPACE:
                weapon_x_pos=char_x_pos+char_width/2-weapon_width/2
                weapon_y_pos=char_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
            
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                key_left_pressed=False
                if key_right_pressed==False: char_to_x=0
                else: char_to_x=char_speed
            if e.key == pygame.K_RIGHT:
                key_right_pressed=False
                if key_left_pressed==False: char_to_x=0
                else: char_to_x=-char_speed

    # 움직임 처리
    char_x_pos += char_to_x*dt
    if char_x_pos<0: char_x_pos=0
    if char_x_pos>screen_width-char_width: char_x_pos=screen_width-char_width
    
    weapons=[[pos[0], pos[1]-weapon_speed] for pos in weapons]
    weapons=[[pos[0], pos[1]] for pos in weapons if pos[1]>0]

    for idx, val in enumerate(balls):
        ball_x=val["pos_x"]
        ball_y=val["pos_y"]
        idx=val["img_idx"]
        ball_size=ball_images[idx].get_rect().size
        ball_width=ball_size[0]
        ball_height=ball_size[1]

        if ball_x<0 or ball_x>screen_width-ball_width:
            val["to_x"]=val["to_x"]*-1
        if ball_y>screen_height-stage_height-ball_height:
            val["to_y"]=val["init_speed"]
        else: val["to_y"] += 0.5

        val["pos_x"] += val["to_x"]
        val["pos_y"] += val["to_y"]

    #collision
    char_rect=char.get_rect()
    char_rect.left=char_x_pos
    char_rect.top=char_y_pos

    for idx, val in enumerate(balls):
        ball_rect=ball_images[val["img_idx"]].get_rect()
        ball_rect.left=val["pos_x"]
        ball_rect.top=val["pos_y"]

        if char_rect.colliderect(ball_rect):
            running=False
            break

        for widx, wval in enumerate(weapons):
            w_rect=weapon.get_rect()
            w_rect.left=wval[0]
            w_rect.top=wval[1]

            if w_rect.colliderect(ball_rect):
                weapon_remove=widx
                ball_remove=idx

                if val["img_idx"]<3:
                    ball_width=ball_rect.size[0]
                    ball_height=ball_rect.size[1]
                    s_ball_rect=ball_images[val["img_idx"]+1].get_rect()
                    s_ball_width=s_ball_rect.size[0]
                    s_ball_height=s_ball_rect.size[1]

                    #ball 2개 입력
                    balls.append({
                        "pos_x": val["pos_x"]+ball_width/2-s_ball_width/2,
                        "pos_y": val["pos_y"]+ball_height/2-s_ball_height/2,
                        "img_idx": val["img_idx"]+1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_speed":ball_speeds[val["img_idx"]+1]
                    })
                    balls.append({
                        "pos_x": val["pos_x"]+ball_width/2-s_ball_width/2,
                        "pos_y": val["pos_y"]+ball_height/2-s_ball_height/2,
                        "img_idx": val["img_idx"]+1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_speed":ball_speeds[val["img_idx"]+1]
                    })
                break
        else:
            continue # 안쪽 for문이 완료되는 경우 실행... 바깥쪽 for문으로....
        break   # 안쪽 for문이 break되는 경우에만 실행... 바깥쪽 for문도 break됨..

    if ball_remove > -1:
        del balls[ball_remove]
        ball_remove=-1
    if weapon_remove > -1:
        del weapons[weapon_remove]
        weapon_remove=-1

    if len(balls)==0:
        game_result="Mission Complete!!"
        running = False
    
    # timer
    timer=game_font.render("Time: {}".format(\
        int(game_time-(pygame.time.get_ticks()-start_ticks)/1000)),True,(255,255,255))
    
    # screen.blit 처리
    screen.blit(background,(0,0))
    for [x,y] in weapons:
        screen.blit(weapon,(x,y))
    for ball in balls:
        screen.blit(ball_images[ball["img_idx"]],(ball["pos_x"],ball["pos_y"]))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(char,(char_x_pos,char_y_pos))
    screen.blit(timer,(10,10))
    
    if game_time-(pygame.time.get_ticks()-start_ticks)/1000<=0:
        game_result="Time Over!!"
        running=False

    pygame.display.update()

msg=game_font.render(game_result, True, (255,255,0))
msg_rect=msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()