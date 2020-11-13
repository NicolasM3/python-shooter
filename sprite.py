import pygame
import time

# classe responsável pelo controle das animações dos personagens
class sprite:
    def __init__(self, player_number, direction):
        # se o player for 1, colocamos a imagem da shotgun
        if(player_number == 1):
            self.path = "images//sprites//shotgun//"
            self.__rotate = False            
        else:
            # se for o jogador dois, passamos a imagem do rifle
            self.path = "images//sprites//rifle//"
            self.__rotate = True
        # setamos as outras variáveis adicionais
        self.direction = direction
        self.count = 0
        self.images = []

        # adicionamos as imagens no vetor        
        for i in range(16):
            nmr = str(i+1).zfill(2)
            img = self.path + f"Armature_run_{nmr}.png"
            self.images.append(img)

    # método responsável pela animação do andar do pinguim
    def move(self, direction, position, tela):
        # mudamos a variavel         
        if(direction == 4 or direction == 0):
            pass
        elif(direction <= 3):
            self.rotate = False
        else:
            self.rotate = True

        # incrementamos 1 no count, para mudar o numero da animacao
        self.count = self.count + 1
        if(self.count >= 16):
            self.count = 0

        self.draw_walk(position, tela)

    # função que para a sprite  na posicao inicial
    def stop(self, position, tela):
        self.count = 0
        self.draw_walk(position, tela)

    # função que realiza a animação de tiro, de acordo com a direção
    def shoot(self, direction, position, tela, is_action):
        if(is_action):
            self.count = 0
        if(direction == 0):
            self.draw_shoot("Armature_jump_shooting_up_", position, tela)
        elif(direction == 1 or direction == 7):
            self.draw_shoot("Armature_jump_shooting_diagonal_up_", position, tela)
        elif(direction == 2 or direction == 6):
            self.draw_shoot("Armature_jump_shooting_forward_", position, tela)
        elif(direction == 3 or direction == 5):
            self.draw_shoot("Armature_jump_shooting_diagonal_down_", position, tela)
        else:
            self.draw_shoot("Armature_jump_shooting_down_", position, tela)

    # propriedade que pega a imagem atual, no vetor de imagens
    @property
    def current_image(self):
        return self.images[self.count]

    # propriedade que indica o lado da imagem
    @property
    def rotate(self):
        return self.__rotate

    # setter para a direção da imagem
    @rotate.setter
    def rotate(self, state):
        self.__rotate = state

    # função que desenha o  andar da animação
    def draw_walk(self, position, tela):
        player_img = pygame.image.load(self.current_image)
        player_img = pygame.transform.flip(player_img, self.rotate, False)
        player_img = pygame.transform.smoothscale(player_img, [ 86, 86 ])
        player_img.set_colorkey((255, 255, 255))
        tela.blit(player_img, (position[0], position[1]))

    # função que desenha o tiro da animação
    def draw_shoot(self, img, position, tela):        
        player_img = pygame.image.load(self.path + img + str(self.count) + ".png")
        player_img = pygame.transform.flip(player_img, self.rotate, False)
        player_img = pygame.transform.smoothscale(player_img, [ 86, 86 ])
        player_img.set_colorkey((255, 255, 255))
        tela.blit(player_img, (position[0], position[1]))

        if(self.count == 8):
            self.count = 0
    