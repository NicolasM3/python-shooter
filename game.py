import pygame
from player import Player
from pygame.locals import *
from threading import Thread
import time

pygame.init()

tela = pygame.display.set_mode((900, 600))
cenario = pygame.image.load("images//background(2).bmp")
pygame.display.set_caption("Shooter")
player_1 = Player()
player1 = pygame.image.load("images//heart1.bmp")

player_2 = Player()
player2 = pygame.image.load("images//heart2.bmp")

tela.blit(cenario, (0, 0))

clock = pygame.time.Clock()


class game:
    def run():
        while True:
            clock.tick(20)
            keys = pygame.key.get_pressed()

            game.try_move(keys)
            game.try_shoot(keys)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            tela.blit(cenario, (0, 0))
            tela.blit(player1, player_1.get_postion())
            tela.blit(player2, player_2.get_postion())
            pygame.display.update()

    def try_shoot(keys):
        if(keys[K_p] and player_1.arrow):
            thread = Thread(target=game.shoot, args=(player_1, player_2))
            thread.start()
        if(keys[K_q] and player_2.arrow):
            thread = Thread(target=game.shoot, args=(player_2, player_1))
            thread.start()

    def try_move(keys):
        walk_x_p1 = (keys[K_RIGHT] - keys[K_LEFT]) * 10
        walk_y_p1 = (keys[K_DOWN] - keys[K_UP]) * 10
        player_1.move((walk_x_p1, walk_y_p1))

        walk_x_p2 = (keys[K_d] - keys[K_a]) * 10
        walk_y_p2 = (keys[K_s] - keys[K_w]) * 10
        player_2.move((walk_x_p2, walk_y_p2))

        
    def shoot(player_shoot, other_player):
        player_shoot.arrow = False

        arr_position = player_shoot.get_postion()
        x, y = arr_position[0], arr_position[1]

        for i in range(100):
            x += 3
            y += 3
            pygame.draw.rect(tela,(0,0,255),(x,y,10,10))
            time.sleep(0.002)
            pygame.display.update()

            target_position = other_player.get_postion()
            if target_position[0] <= x <= target_position[0] + 48 and target_position[1] <= y <= target_position[1] + 48:
                print('Ganhou')

        player_shoot.arrow = True