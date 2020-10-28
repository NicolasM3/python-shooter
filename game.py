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

player_2 = Player((800, 500), 7)
player2 = pygame.image.load("images//heart2.bmp")

tela.blit(cenario, (0, 0))

clock = pygame.time.Clock()

class game:
    def run():
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

            pygame.display.update()

    def try_shoot(keys):
        game.handle_shoot(player_1, player_2, keys[K_p])
        game.handle_shoot(player_2, player_1, keys[K_q])

    def try_move(keys):
        walk_x_p1 = (keys[K_RIGHT] - keys[K_LEFT]) * 10
        walk_y_p1 = (keys[K_DOWN] - keys[K_UP]) * 10
        if(not(walk_x_p1 == 0 and walk_y_p1 == 0)):
            player_1.move((walk_x_p1, walk_y_p1))

        
        walk_x_p2 = (keys[K_d] - keys[K_a]) * 10
        walk_y_p2 = (keys[K_s] - keys[K_w]) * 10
        if(not(walk_x_p2 == 0 and walk_y_p2 == 0)):
            player_2.move((walk_x_p2, walk_y_p2))


    def handle_shoot(player_shoot, other_player, key):
        if(key and player_shoot.arrow.state == 0):
            player_shoot.shoot()
        if(player_shoot.arrow.state == 1):
            pygame.draw.rect(tela,(0,0,255),(player_shoot.arrow.position[0], player_shoot.arrow.position[1], 10, 10))
            pygame.display.update()
            player_shoot.arrow.move()
        if(player_shoot.arrow.state == 2):
            pygame.draw.rect(tela,(0,0,255),(player_shoot.arrow.position[0], player_shoot.arrow.position[1], 10, 10))
            pygame.display.update()
        


    # def shoot(player_shoot, other_player):
    #     player_shoot.arrow = False
    #     bullet = shoot(player_shoot.direction, [player_shoot.position[0], player_shoot.position[1]])
    #     for i in range(100):
    #         bullet.move()
    #         x, y = bullet.position
    #         pygame.draw.rect(tela,(0,0,255),(x, y,10,10))
    #         time.sleep(0.002)
    #         pygame.display.update()

    #         target_position = other_player.position
    #         if target_position[0] <= x <= target_position[0] + 48 and target_position[1] <= y <= target_position[1] + 48:
    #             print('Ganhou')

    #     player_shoot.arrow = True


    # def shoot(player_shoot, other_player):
    #     player_shoot.arrow = False
    #     bullet = shoot(player_shoot.direction, [player_shoot.position[0], player_shoot.position[1]])
