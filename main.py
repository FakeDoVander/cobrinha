
import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time
import recor
pygame.init()

width = 600
height = 500
x_snake = width / 2
y_snake = height / 2

velocity = 5
x_control = velocity
y_control = 0

x_bunny = randint(40, 450)
y_bunny = randint(60, 450)
x_bunny2 = randint(40, 450)
y_bunny2 = randint(60, 450)

points = count = walls = nnroom = 0
nroom = 1
 
fonts = pygame.font.SysFont("arial", 20, True, False)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()
snake_list = []

initial_length = 3

kill = False


def increase_snake(snake_list):
    for Xey in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), (Xey[0], Xey[1], 20, 20))


def reiniciar_jogo():
    global points, initial_length, x_snake, y_snake, x_bunny, y_bunny, head_list, snake_list, kill, velocity, walls, count, x_bunny2, y_bunny2, nnroom, nroom
    initial_length = 3
    x_snake = width / 2
    y_snake = height / 2
    velocity = 5
    count = 0
    walls = 0
    nnroom = 0
    nroom = 1
    snake_list = []
    head_list = []
    points = 0
    x_bunny = randint(60, 400)
    y_bunny = randint(60, 400)
    x_bunny2 = randint(60, 400)
    y_bunny2 = randint(60, 400)
    kill = False


while True:
    clock.tick(20)
    if points >= 0:
        screen.fill((60, 90, 0))
    if points >= 10:
        screen.fill((70, 100, 0))
    if points >= 20:
        screen.fill((80, 120, 0))
    if points >= 30:
        screen.fill((90, 130, 0))
    if points >= 40:
        screen.fill((100, 140, 0))
    if points >= 50:
        screen.fill((120, 150, 0))
    if points >= 60:
        screen.fill((130, 160, 0))
    if points >= 70:
        screen.fill((150, 170, 0))
    if points >= 80:
        screen.fill((160, 180, 0))
    if points >= 90:
        screen.fill((0, 0, 0))
    msg = f"Pontos: {points}"
    text_formatado = fonts.render(msg, True, (255, 255, 255))
    credit = "CL"
    text_credit = fonts.render(credit, True, (255, 255, 255))
    trecord = f"Maior Record: {record.record}"
    text_trecord = fonts.render(trecord, True, (255, 255, 255))
    logo = "JOGO DA COBRINHA"
    text_logo = fonts.render(logo, True, (255, 255, 0))
    room = f"Fase: {nroom}"
    text_room = fonts.render(room, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_control == velocity:
                    pass
                else:
                    x_control = -velocity
                    y_control = 0
            if event.key == K_RIGHT:
                if x_control == -velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0
            if event.key == K_UP:
                if y_control == velocity:
                    pass
                else:
                    x_control = 0
                    y_control = -velocity
            if event.key == K_DOWN:
                if y_control == -velocity:
                    pass
                else:
                    x_control = 0
                    y_control = velocity
            if event.key == K_a:
                if x_control == velocity:
                    pass
                else:
                    x_control = -velocity
                    y_control = 0
            if event.key == K_d:
                if x_control == -velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0
            if event.key == K_w:
                if y_control == velocity:
                    pass
                else:
                    x_control = 0
                    y_control = -velocity
            if event.key == K_s:
                if y_control == -velocity:
                    pass
                else:
                    x_control = 0
                    y_control = velocity

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

    snake = pygame.draw.rect(screen, (0, 155, 0), (x_snake, y_snake, 20, 20))

    bunny = pygame.draw.rect(screen, (255, 255, 255),(x_bunny, y_bunny - 5, 8, 15))
    bunny = pygame.draw.rect(screen, (255, 255, 255),(x_bunny + 12, y_bunny - 5, 8, 15))
    bunny = pygame.draw.rect(screen, (255, 255, 255),(x_bunny, y_bunny, 20, 20))

    par1 = pygame.draw.rect(screen, (70, 145, 0), (width - 10, 0, 10, 1000))
    par2 = pygame.draw.rect(screen, (70, 145, 0), (width - width, 0, 10, 1000))
    par3 = pygame.draw.rect(screen, (70, 145, 0),(0, height - height, 1000, 40))
    par4 = pygame.draw.rect(screen, (70, 145, 0), (0, height - 30, 1000, 30))

    if snake.colliderect(bunny):
        x_bunny = randint(60, 450)
        y_bunny = randint(60, 450)
        points = points + 1
        count = count + 1
        walls = walls + 1
        nnroom = nnroom + 1
        if points > record.record:
            record.record = record.record + 1
        elif points <= record.record:
            pass
        if velocity <= 8:
            velocity = velocity + 1
        if velocity >= 8:
            pass
        initial_length = initial_length + 3

    if count >= 10:
        bunny2 = pygame.draw.rect(screen, (55, 0, 255),(x_bunny2, y_bunny2 - 5, 8, 15))
        bunny2 = pygame.draw.rect(screen, (55, 0, 255),(x_bunny2 + 12, y_bunny2 - 5, 8, 15))
        bunny2 = pygame.draw.rect(screen, (55, 0, 255),(x_bunny2, y_bunny2, 20, 20))
        if snake.colliderect(bunny2):
            x_bunny2 = randint(60, 400)
            y_bunny2 = randint(60, 400)
            velocity = velocity + 1
            points = points + 3
            nnroom = nnroom + 3
            if points > record.record:
                record.record = record.record + 3
            elif points <= record.record:
                pass
            initial_length = initial_length + 5
            count = count - 10

    if nnroom == 10:
      nroom = nroom + 1
      nnroom = nnroom - 10
     
    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    snake_list.append(head_list)

    if snake_list.count(head_list) > 1 or snake.colliderect(par1) or snake.colliderect(par2) or snake.colliderect(par3) or snake.colliderect(par4):
        fonts1 = pygame.font.SysFont("arial", 20, True, False)
        fonts2 = pygame.font.SysFont("arial", 30, True, False)
        rdepoints = f"Você fez {points} pontos"
        if points < 90:  
          mensagem = "Gamer Over"
          novamente = "Para jogar novamente pressione R."
          maiorrecord = f"Maior record: {record.record}"
        if points > 90:
          mensagem = "Parabens"
          novamente = "Para jogar novamente pressione R."
          maiorrecord = f"Maior record: {record.record}"
        formatted_text1 = fonts1.render(rdepoints, True, (255, 255, 255))
        formatted_text2 = fonts2.render(mensagem, True, (255, 255, 255))
        formatted_text3 = fonts1.render(novamente, True, (255, 255, 255))
        formatted_text4 = fonts1.render(maiorrecord, True, (255, 255, 255))
        ret_text1 = formatted_text1.get_rect()
        ret_text2 = formatted_text2.get_rect()
        ret_text3 = formatted_text3.get_rect()
        ret_text4 = formatted_text4.get_rect()
        kill = True
        while kill:
            time.sleep(1)
            screen.fill((20, 70, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        time.sleep(0.5)
                        reiniciar_jogo()
            ret_text1.center = (width / 2, height - 200)
            ret_text2.center = (width / 2, height / 3)
            ret_text3.center = (width / 2, height - 300)
            ret_text4.center = (width / 2, height - 100)
            screen.blit(formatted_text1, ret_text1)
            screen.blit(formatted_text2, ret_text2)
            screen.blit(formatted_text3, ret_text3)
            screen.blit(formatted_text4, ret_text4)
            pygame.display.update()

    if x_snake > width:
        x_snake = width
    if x_snake < 1:
        x_snake = -width
    if y_snake > height:
        y_snake = height
    if y_snake < 1:
        y_snake = -height

    if len(snake_list) > initial_length:
        del snake_list[0]
    increase_snake(snake_list)
    screen.blit(text_formatado, (10, 10))
    screen.blit(text_trecord, (width - 490, height - 20))
    screen.blit(text_credit, (width - 30, height - 20))
    screen.blit(text_logo, (width - 220, 10))
    screen.blit(text_room, (width - 320, 10))
    pygame.display.update()
