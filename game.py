import pygame
from player import Player
from pygame.locals import *
from threading import Thread
import time

pygame.init()

tela = pygame.display.set_mode((900, 600))
cenario = pygame.image.load("images//background(2).bmp")
pygame.display.set_caption("Shooter")

player_1 = Player((100, 100), 2)
player1 = pygame.image.load("images//heart1.bmp")
player1.set_colorkey((255, 255, 255))

player_2 = Player((800, 500), 7)
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
            tela.blit(player1, (player_1.position[0], player_1.position[1]))
            tela.blit(player2, (player_2.position[0], player_2.position[1]))

            game.try_move(keys)
            game.try_shoot(keys)
    
            if(has_objects_collided(player_1, player_2)):
                cont = cont + 1
                print(cont)

            pygame.display.update()

    def try_shoot(keys):
        game.handle_shoot(player_1, player_2, keys[K_p])
        game.handle_shoot(player_2, player_1, keys[K_q])

    def try_move(keys):
        walk_x_p1 = (keys[K_RIGHT] - keys[K_LEFT])
        walk_y_p1 = (keys[K_DOWN] - keys[K_UP]) 
        if(not(walk_x_p1 == 0 and walk_y_p1 == 0)):
            player_1.move((walk_x_p1, walk_y_p1))

        
        walk_x_p2 = (keys[K_d] - keys[K_a])
        walk_y_p2 = (keys[K_s] - keys[K_w])
        if(not(walk_x_p2 == 0 and walk_y_p2 == 0)):
            player_2.move((walk_x_p2, walk_y_p2))


    def handle_shoot(player_shoot, other_player, key):
        if(key and player_shoot.arrow.state == 0):
            player_shoot.shoot()
        if(player_shoot.arrow.state == 1):
            pygame.draw.rect(tela,(0,0,255),(player_shoot.arrow.position[0], player_shoot.arrow.position[1], 10, 10))
            pygame.display.update()
            player_shoot.arrow.move()

            new_position = player_shoot.arrow.position

            if(player_shoot.arrow.position[0] >= 900):
                new_position[0] = 1
            if(player_shoot.arrow.position[1] >= 600):
                new_position[1] = 1
            if(player_shoot.arrow.position[0] <= 0):
                new_position[0] = 900
            if(player_shoot.arrow.position[1] <= 0):
                new_position[1] = 600

            player_shoot.arrow.position = new_position

            
        if(player_shoot.arrow.state == 2):
            pygame.draw.rect(tela,(255,0,0),(player_shoot.arrow.position[0], player_shoot.arrow.position[1], 10, 10))
            pygame.display.update()
        