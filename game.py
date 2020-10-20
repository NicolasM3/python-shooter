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
        if(keys[K_p] and player_1.get_arrow()):
            thread = Thread(target=game.shoot, args=(player_1, player_2))
            thread.start()
        if(keys[K_q] and player_2.get_arrow()):
            thread = Thread(target=game.shoot, args=(player_2, player_1))
            thread.start()

    def try_move(keys):
        if(keys[K_LEFT]):
                player_1.move((-10, 0))
        if(keys[K_RIGHT]):
            player_1.move((10, 0))
        if(keys[K_UP]):
            player_1.move((0, -10))
        if(keys[K_DOWN]):
            player_1.move((0, 10))
        if(keys[K_a]):
            player_2.move((-10, 0))
        if(keys[K_d]):
            player_2.move((10, 0))
        if(keys[K_w]):
            player_2.move((0, -10))
        if(keys[K_s]):
            player_2.move((0, 10))

    def shoot(player_shoot, other_player):
        player_shoot.defarrow(False)

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

        player_shoot.defarrow(True)