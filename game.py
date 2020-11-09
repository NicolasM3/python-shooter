import pygame
from player import Player
from pygame.locals import *
from threading import Thread
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("soundtrack//Titan Souls - 02 Titans.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

tela = pygame.display.set_mode((900, 600))
initial_menu = pygame.image.load("images//menu.png")
esc_menu = pygame.image.load("images//esc_menu.png")
cenario = pygame.image.load("images//background(2).bmp")
winner_1 = pygame.image.load("images//player_1_winner.png")
winner_2 = pygame.image.load("images//player_2_winner.png")
pygame.display.set_caption("Shooter")

player_1 = Player(1, (100, 100), 2)
heart_player1 = pygame.image.load("images//heart1.bmp")
heart_player1.set_colorkey((255, 255, 255))

player_2 = Player(2, (800, 500), 7)
heart_player2 = pygame.image.load("images//heart2.bmp")
heart_player2.set_colorkey((255, 255, 255))

clock = pygame.time.Clock()


def has_objects_collided(object_1, object_2):
    tam = 48
    if(object_1.position[0] + tam >= object_2.position[0] >= object_1.position[0]
        or object_2.position[0] + tam >= object_1.position[0] >= object_2.position[0]):
        if(object_1.position[1] + tam >= object_2.position[1] >= object_1.position[1]
            or object_2.position[1] + tam >= object_1.position[1] >= object_2.position[1]):
            return True
    
    return False

def draw_player(player):
    player_img = pygame.image.load("images//" + player.sprite.current_image)
    player_img = pygame.transform.flip(player_img, player.sprite.rotate, False)
    player_img = pygame.transform.smoothscale(player_img, [ 86, 86 ])
    player_img.set_colorkey((255, 255, 255))
    tela.blit(player_img, (player.position[0], player.position[1]))

def draw_life():
    player1_life = player_1.life
    player2_life = player_2.life

    for i in range(0, player2_life):
        tela.blit(heart_player2, (750 + (i * 40), 25))

    for i in range(0, player1_life):
        tela.blit(heart_player1, (0 + (i * 40), 25))

def draw_menu(img):
    while True:
        tela.blit(img, (0,0))
        clock.tick(20)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if keys[K_SPACE] != 0:
            break
        if keys[K_q] != 0:
            pygame.quit()
        pygame.display.update()


def show_winner(winner_img):
    tela.blit(winner_img, (0, 0))
    pygame.display.update()
    clock.tick(10000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
            
class game:
    def run():
        draw_menu(initial_menu)

        cont = 0
        while True:
            clock.tick(20)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            tela.blit(cenario, (0, 0))

            if(keys[K_ESCAPE] != 0):
                draw_menu(esc_menu)

            game.try_move(keys[K_RIGHT], keys[K_LEFT], keys[K_UP], keys[K_DOWN], player_2, tela)
            game.try_move(keys[K_d], keys[K_a], keys[K_w], keys[K_s], player_1, tela)

            game.handle_shoot(player_1, player_2, keys[K_q])
            game.handle_shoot(player_2, player_1, keys[K_p])
    
            draw_life()

            if(player_1.life == 0):
                show_winner(winner_2)
            elif(player_2.life == 0):
                show_winner(winner_1)

            pygame.display.update()

        

    def try_move(k_r, k_l, k_u, k_d, player, tela):
        walk_x = (k_r - k_l)
        walk_y = (k_d - k_u) 
        if(not(walk_x == 0 and walk_y == 0)):
            player.move((walk_x, walk_y), tela)
            player.position = game.calculate_new_pos(player)
        else:
            player.idle(tela)

    def handle_shoot(player_shoot, other_player, key):
        if(key and player_shoot.arrow.state == 0):
            player_shoot.shoot(tela)
        if(player_shoot.arrow.state == 1):
            game.draw_arrow(player_shoot)
            player_shoot.arrow.move()
            player_shoot.arrow.position = game.calculate_new_pos(player_shoot.arrow)

            if(has_objects_collided(player_shoot.arrow, other_player)):
                other_player.life = 1
                player_shoot.arrow.state = 2
        
        if(player_shoot.arrow.state == 2):
            if(has_objects_collided(player_shoot, player_shoot.arrow)):
                player_shoot.arrow.state = 0
            else:
                game.draw_arrow(player_shoot)

    def draw_arrow(player):
        arrow_img = pygame.image.load("images//" + player.arrow.current_image)
        arrow_img.set_colorkey((255, 255, 255))
        tela.blit(arrow_img, (player.arrow.position[0], player.arrow.position[1]))
        pygame.display.update()

    def calculate_new_pos(object):
        new_position = object.position
        if(object.position[0] >= 885):
            new_position[0] = 6
        if(object.position[1] >= 585):
            new_position[1] = 6
        if(object.position[0] <= -15):
            new_position[0] = 880
        if(object.position[1] <= -15):
            new_position[1] = 580
        return new_position
