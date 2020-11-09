
import pygame
from player import Player
from pygame.locals import *
from threading import Thread
import time

pygame.init()                                               # iniciando pygame
pygame.mixer.init()                                         # iniciando som

# carregando e configurando o som
pygame.mixer.music.load("soundtrack//Titan Souls - 02 Titans.mp3")  
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

# iniciando e configurando a tela
tela = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Shooter")

# carregando imagens usadas
initial_menu = pygame.image.load("images//menu.png")            # menu inicial
esc_menu = pygame.image.load("images//esc_menu.png")            # munu esc
cenario = pygame.image.load("images//background(2).bmp")        # cenario
winner_1 = pygame.image.load("images//player_1_winner.png")     # vencedor
winner_2 = pygame.image.load("images//player_2_winner.png")     
heart_player1 = pygame.image.load("images//heart1.bmp")         #corações
heart_player2 = pygame.image.load("images//heart2.bmp")
heart_player1.set_colorkey((255, 255, 255))                  # Retirando a imagem do fundo
heart_player2.set_colorkey((255, 255, 255))

# iniciando player com o número do player, position, e direção
player_1 = Player(1, (100, 100), 2)
player_2 = Player(2, (800, 500), 7)


clock = pygame.time.Clock()                                  # Iniciando clock


# Verifica se dois objetos colidiram
# object_1 - objeto um para verificar
# object_2 - objeto dois para verificar
def has_objects_collided(object_1, object_2):
    tam = 48                                                # hit box dos objetos 

    # Verifica se uma área do objeto_1 esta dentro do objeto_2
    if(object_1.position[0] + tam >= object_2.position[0] >= object_1.position[0]
        or object_2.position[0] + tam >= object_1.position[0] >= object_2.position[0]):
        if(object_1.position[1] + tam >= object_2.position[1] >= object_1.position[1]
            or object_2.position[1] + tam >= object_1.position[1] >= object_2.position[1]):
            return True
    
    return False


# Desenha o player na tela
# Player a ser desenhado
def draw_player(player):
    player_img = pygame.image.load("images//" + player.sprite.current_image)          # carrega o spite a se utilizada
    player_img = pygame.transform.flip(player_img, player.sprite.rotate, False)       # da o flip na imagem para a direção atual 
    player_img = pygame.transform.smoothscale(player_img, [ 86, 86 ])                 # redimensiona o personagem               
    player_img.set_colorkey((255, 255, 255))                                          # retira o fundo da imagem
    tela.blit(player_img, (player.position[0], player.position[1]))                   # desenha

# Desenha a quantidade de vida de cada personagem na tela
def draw_life():
    # pega a quantidade de vida de cada personagem
    player1_life = player_1.life                                     
    player2_life = player_2.life

    # desenha n vezes os corações na tela
    # n = quantidade de vida dos personages
    for i in range(0, player2_life):
        tela.blit(heart_player2, (750 + (i * 40), 25))              # desenha 40 px para a frente do ultimo coração

    for i in range(0, player1_life):
        tela.blit(heart_player1, (0 + (i * 40), 25))                # desenha 40 px para a frente do ultimo coração

# desenha o menu na tela
# img - imagem a ser desenhada
def draw_menu(img):
    while True:                                                     # fica infinitamente na tela
        # desenha na tela
        tela.blit(img, (0,0))
        pygame.display.update()
        clock.tick(20)

        # verifica se não apertou o botão de fechar a janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # verifica se não apertou espaço - para inicia
        # ou q para sair
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] != 0:
            break
        if keys[K_q] != 0:
            pygame.quit()
        

# desenha a tela de vitoria para o vencedor
# winner_img - imagem a ser desenhada
def show_winner(winner_img):
    # desenha a imagem passada
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
    # metodo com o loop principal
    def run():
        draw_menu(initial_menu)                         # desenha o menu inicial                       
        cont = 0
        while True:                                     # loop principal
            clock.tick(20)
            keys = pygame.key.get_pressed()

            # verifica se não apertou o botão de fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            tela.blit(cenario, (0, 0))                                  # desenha o cenario

            if(keys[K_ESCAPE] != 0):                                    # verifica se apertou o botão de pause
                draw_menu(esc_menu)

            # tenta se mover, mandam as teclas e onde desenhar
            # o metodo verifica se ta se movendo tomando as devidas responsabilidades
            game.try_move(keys[K_RIGHT], keys[K_LEFT], keys[K_UP], keys[K_DOWN], player_2, tela)
            game.try_move(keys[K_d], keys[K_a], keys[K_w], keys[K_s], player_1, tela)

            # tenta atirar para cada player, mandam o player que atirou, o possível alvo
            # e a telca
            # o metodo verifica se ta atirando tomando as devidas responsabilidades
            game.handle_shoot(player_1, player_2, keys[K_q])
            game.handle_shoot(player_2, player_1, keys[K_p])
    
            draw_life()                                                 # desenha a quatidade de vida

            if(player_1.life == 0):                                     # verifica se algum player ganhou
                show_winner(winner_2)
            elif(player_2.life == 0):
                show_winner(winner_1)

            pygame.display.update()                                     # atualiza a tela

        
    # Verfica se esta se movendo e faz as ações necessarias apartir disso
    # k_r - tecla de movimento para a direita
    # k_l - tecla de movimento para a esquerda
    # k_u - tecla de movimento para cima
    # k_d - tecla de movimento para baixo
    # player que tanta o movimento
    # tela em que sera desenhado
    def try_move(k_r, k_l, k_u, k_d, player, tela):
        # pega a direção X e Y com base nas teclas apertadas
        walk_x = (k_r - k_l)                                    
        walk_y = (k_d - k_u) 
        if(not(walk_x == 0 and walk_y == 0)):                               # se o player se moveu
            player.move((walk_x, walk_y), tela)                             # muda a posição dele
            player.position = game.calculate_new_pos(player)                # verifica se a nova posição é válida
        else:                                                               # se não se moveu
            player.idle(tela)                                               # chama a animação idle do player

    # Verifica se o player esta atirando
    # player_shoot - player que esta atirando
    # other_player - player alvo do tiro
    # tecla para atirar
    def handle_shoot(player_shoot, other_player, key):
        if(key and player_shoot.arrow.state == 0):                          # se a tecla foi apertada e pode atirar      
            player_shoot.shoot(tela)                                        # atira
        if(player_shoot.arrow.state == 1):                                  # se a flecha esta em movimento
            game.draw_arrow(player_shoot)                                   
            player_shoot.arrow.move()
            player_shoot.arrow.position = game.calculate_new_pos(player_shoot.arrow)    # verifica se é uma posição valida

            if(has_objects_collided(player_shoot.arrow, other_player)):     # se acertou a flecha
                other_player.life = 1
                player_shoot.arrow.state = 2
        
        if(player_shoot.arrow.state == 2):                                  # se a flecha esta no chão
            if(has_objects_collided(player_shoot, player_shoot.arrow)):     # se o player que atirou colidiu com ela
                player_shoot.arrow.state = 0                                # pega a flecha
            else:                                                           # se não
                game.draw_arrow(player_shoot)                               # desenha ela

    # desenha a flecha 
    # player - player que atirou a flecha
    def draw_arrow(player):                                                 
        # carrega e configura a imagem
        arrow_img = pygame.image.load("images//" + player.arrow.current_image)
        arrow_img.set_colorkey((255, 255, 255))

        # desenha a atualiza a tela
        tela.blit(arrow_img, (player.arrow.position[0], player.arrow.position[1]))
        pygame.display.update()

    # verifiac se a posição de algo é válida (ex: saiu da tela)
    # object para verifica a posição
    def calculate_new_pos(object):
        new_position = object.position

        # se não é maior o menor que os limites da tela
        # se for atualiza para a posição correta
        if(object.position[0] >= 885):
            new_position[0] = 6
        if(object.position[1] >= 585):
            new_position[1] = 6
        if(object.position[0] <= -15):
            new_position[0] = 880
        if(object.position[1] <= -15):
            new_position[1] = 580
        return new_position
