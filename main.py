import pygame
from player import Player
from pygame.locals import *

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

while True:
    clock.tick(20)

    keys = pygame.key.get_pressed()

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


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
       
    tela.blit(cenario, (0, 0))
    tela.blit(player1, player_1.get_postion())
    tela.blit(player2, player_2.get_postion())
    pygame.display.update()

    pygame.event.pump()
