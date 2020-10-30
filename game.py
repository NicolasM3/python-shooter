import pygame
from player import Player
from pygame.locals import *
from threading import Thread
import time

pygame.init()

tela = pygame.display.set_mode((900, 600))
cenario = pygame.image.load("images//background(2).bmp")
pygame.display.set_caption("Shooter")

player_1 = Player(1, (100, 100), 2)

player_2 = Player(2, (800, 500), 7)
player2 = pygame.image.load("images//heart2.bmp")
player2.set_colorkey((255, 255, 255))

tela.blit(cenario, (0, 0))

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

class game:
    def run():
        cont = 0
        while True:
            clock.tick(20)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            tela.blit(cenario, (0, 0))

            #draw_player(player_1)
            #draw_player(player_2)

            game.try_move(keys[K_RIGHT], keys[K_LEFT], keys[K_UP], keys[K_DOWN], player_1, tela)
            game.try_move(keys[K_d], keys[K_a], keys[K_w], keys[K_s], player_2, tela)

            game.handle_shoot(player_1, player_2, keys[K_p])
            game.handle_shoot(player_2, player_1, keys[K_q])
    
            if(has_objects_collided(player_1, player_2)):
                cont = cont + 1
                print(cont)

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
                print('Ganhou')
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
