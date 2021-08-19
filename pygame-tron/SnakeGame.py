#VINÍCIUS MARTINS COTRIM 19040
#MANUELA VICENTE BENASSI 19184 

import pygame, random, sys
from pygame import mixer
from pygame.locals import *

pygame.init()
mixer.init()

pygame.display.set_caption('TRON')

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

bg_home = pygame.image.load('page_home.png').convert()
bg_home = pygame.transform.scale(bg_home, (602, 602))

bg_about = pygame.image.load('page_about.png').convert()
bg_about = pygame.transform.scale(bg_about, (602, 602))

bg_help = pygame.image.load('page_help.png').convert()
bg_help = pygame.transform.scale(bg_help, (602, 602))

bg_game = pygame.image.load('page_game.png').convert()
bg_game = pygame.transform.scale(bg_game, (602, 602))

#VARIAVEIS PARA A LOGICA DO JOGO

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

white = (255, 255, 255) 
verde = (0, 255, 0) 
azul = (102, 163, 242)
laranja = (255, 134, 1) 
red = (242, 48, 48)

#DEF'S QUE DESENHAM AS TELAS DE JOGO: PLAY, ABOUT E HELP

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    click = False

    button_1 = pygame.Rect(200, 300, 190, 50)
    button_2 = pygame.Rect(200, 360, 190, 50)
    button_3 = pygame.Rect(200, 420, 190, 50) 

    while True:
        screen.blit(bg_home, (0,-2)) 

        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play(0)
                game()
            pygame.draw.rect(screen, laranja, button_1)
            

        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play(0)
                help()
            pygame.draw.rect(screen, laranja, button_2)

        if button_3.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play(0)
                about()
            pygame.draw.rect(screen, laranja, button_3)
        
        draw_text('PLAY', pygame.font.Font("Gamer.ttf", 50), (255, 255, 255), screen, 220, 300) 
        draw_text('HELP', pygame.font.Font("Gamer.ttf", 50), (255, 255, 255), screen, 220, 360) 
        draw_text('ABOUT', pygame.font.Font("Gamer.ttf", 50), (255, 255, 255), screen, 220, 420) 

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def about():
    running = True
    screen.blit(bg_about, (-1,-2))

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
    
        pygame.display.update()
        clock.tick(60)
    
def help():
    running = True
    screen.blit(bg_help, (-1,-2))

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)

def game():

    play_again = True

    while play_again:

        p1_car_surface = pygame.image.load("car_blue.png")
        p1_car_surface = pygame.transform.scale(p1_car_surface, (30, 30))
        p1_car_aux = p1_car_surface

        p1_car = pygame.Rect(170, 280, 30, 30)

        p1_wall_skin = pygame.Surface((10,10))
        p1_wall_skin.fill(azul)

        p1_car_x = 170
        p1_car_y = 280
        p1_direction = -1
        p1_press = False
        p1_wall = []

        p2_car_surface = pygame.image.load("car_orange.png")
        p2_car_surface = pygame.transform.scale(p2_car_surface, (30, 30))
        p2_car_aux = p2_car_surface

        p2_car = pygame.Rect(270, 280, 30, 30)

        p2_wall_skin = pygame.Surface((10,10))
        p2_wall_skin.fill(laranja)

        p2_car_x = 270
        p2_car_y = 280
        p2_direction = -1
        p2_press = False
        p2_wall = []

        game_over = False

        countdown()
  
        pygame.mixer.music.load("theme.wav") #ARRUMA ISSO
        pygame.mixer.music.play(0)

        while not game_over:

            screen.fill((0,0,0))
            screen.blit(bg_game, (0,0))
            
            p1_car.topleft = (p1_car_x, p1_car_y)
            p2_car.topleft = (p2_car_x, p2_car_y)
            
            for wall in p1_wall:
                 pygame.draw.rect(screen, azul, wall)

            for wall in p2_wall:
                 pygame.draw.rect(screen, laranja, wall)

            screen.blit(p1_car_surface, p1_car)
            screen.blit(p2_car_surface, p2_car)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_over = True
                        play_again = False

                    if event.key == K_SPACE:
                        p1_press = not p1_press

                    if event.key == K_RSHIFT:
                        p2_press = not p2_press
                
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_w]:
                p1_car_surface = pygame.transform.rotate(p1_car_aux, 0)
                p1_direction = UP

            if pressed[pygame.K_s]:
                p1_car_surface = pygame.transform.rotate(p1_car_aux, 180)
                p1_direction = DOWN

            if pressed[pygame.K_a]:
                p1_car_surface = pygame.transform.rotate(p1_car_aux, 90)
                p1_direction = LEFT
            
            if pressed[pygame.K_d]:
                p1_car_surface = pygame.transform.rotate(p1_car_aux, 270)
                p1_direction = RIGHT

            if pressed[pygame.K_UP]:
                p2_car_surface = pygame.transform.rotate(p2_car_aux, 0)
                p2_direction = UP
                
            if pressed[pygame.K_DOWN]:
                p2_car_surface = pygame.transform.rotate(p2_car_aux, 180)
                p2_direction = DOWN

            if pressed[pygame.K_LEFT]:
                p2_car_surface = pygame.transform.rotate(p2_car_aux, 90)
                p2_direction = LEFT
            
            if pressed[pygame.K_RIGHT]:
                p2_car_surface = pygame.transform.rotate(p2_car_aux, 270)
                p2_direction = RIGHT
            
            if p1_press:
                p1_wall.append(pygame.Rect(p1_car.centerx-5, p1_car.centery-5, 10, 10))

            if p2_press:
                p2_wall.append(pygame.Rect(p2_car.centerx-5, p2_car.centery-5, 10, 10))

            if p1_direction == UP:
                p1_car_y -= 1

            if p1_direction == LEFT:
                p1_car_x -= 1

            if p1_direction == DOWN:
                p1_car_y += 1

            if p1_direction == RIGHT:
                p1_car_x += 1
            
            if p2_direction == UP:
                p2_car_y -= 1

            if p2_direction == LEFT:
                p2_car_x -= 1

            if p2_direction == DOWN:
                p2_car_y += 1

            if p2_direction == RIGHT:
                p2_car_x += 1

            if collision(p1_car, p2_wall) or p1_car_x > 570 or p1_car_x < 0 or p1_car_y > 570 or p1_car_y < 0:
                game_over = True        
                play_again = end_game(2)

            if collision(p2_car, p1_wall) or p2_car_x > 570 or p2_car_x < 0 or p2_car_y > 570 or p2_car_y < 0:
                game_over = True        
                play_again = end_game(1)

            if p1_car.colliderect(p2_car):
                game_over = True        
                play_again = end_game(3)

            pygame.display.update()
            clock.tick(120)

    pygame.mixer.music.pause()

def countdown():
    timer = pygame.time.Clock()
    seconds = 5

    pygame.mixer.music.load("countdown.mp3")
    pygame.mixer.music.play(0)

    while seconds > 0:
        screen.blit(bg_game, (0,0))
        draw_text(str(seconds), pygame.font.Font("Gamer.ttf", 150), (255, 255, 255), screen, 270, 220)
        
        seconds -= 1
        pygame.display.update()
        timer.tick(1)
    
    
    pygame.mixer.music.stop()

def end_game(winner):
    
    pygame.mixer.music.load("explosao.wav")
    pygame.mixer.music.play(0)

    running = True
    click = False

    menu = pygame.Rect(150, 300, 150, 50) 
    again = pygame.Rect(310, 300, 150, 50) 

    if winner == 3:
        winner = "Ops, it's a tie"
    else:
        winner = "Player {} won!".format(winner)
    
    while running:

        mx, my = pygame.mouse.get_pos()

        if menu.collidepoint((mx, my)):
            if click:
                return False

        if again.collidepoint((mx, my)):
            if click:
                return True             

        pygame.draw.rect(screen, laranja, menu)
        pygame.draw.rect(screen, laranja, again)

        draw_text("Menu", pygame.font.Font("Gamer.ttf", 50), white, screen, 180, 302)
        draw_text("Again", pygame.font.Font("Gamer.ttf", 50), white, screen, 340, 302)

        draw_text("GAME OVER", pygame.font.Font("Gamer.ttf", 120), red, screen, 100, 120)
        draw_text(winner, pygame.font.Font("Gamer.ttf", 55), verde, screen, 180, 220)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def collision(car, wall):
    for part in wall:
        if car.colliderect(part):
            return True

    return False 

main()