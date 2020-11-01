import pygame
import time
class sprite:
    def __init__(self, player_number, direction):
        if(player_number == 1):
            self.path = "images//sprites//shotgun//"
            self.__rotate = False            
        else:
            self.path = "images//sprites//rifle//"
            self.__rotate = True

        self.direction = direction
        self.count = 0
        self.images = []        
        for i in range(16):
            nmr = str(i+1).zfill(2)
            img = self.path + f"Armature_run_{nmr}.png"
            self.images.append(img)

    def move(self, direction, position, tela):
        if(direction == 4 or direction == 0):
            pass
        elif(direction <= 3):
            self.rotate = False
        else:
            self.rotate = True

        self.count = self.count + 1
        if(self.count >= 16):
            self.count = 0

        self.draw_walk(position, tela)

    def stop(self, position, tela):
        self.count = 0
        self.draw_walk(position, tela)

    def shoot(self, direction, position, tela):
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

    @property
    def current_image(self):
        return self.images[self.count]

    @property
    def rotate(self):
        return self.__rotate

    @rotate.setter
    def rotate(self, state):
        self.__rotate = state

    def draw_walk(self, position, tela):
        player_img = pygame.image.load(self.current_image)
        player_img = pygame.transform.flip(player_img, self.rotate, False)
        player_img = pygame.transform.smoothscale(player_img, [ 86, 86 ])
        player_img.set_colorkey((255, 255, 255))
        tela.blit(player_img, (position[0], position[1]))

    def draw_shoot(self, img, position, tela):
        for i in range(16):
            player_img = pygame.image.load(self.path + img + str(i//2) + ".png")
            player_img = pygame.transform.flip(player_img, self.rotate, False)
            player_img = pygame.transform.smoothscale(player_img, [ 86, 86 ])
            player_img.set_colorkey((255, 255, 255))
            tela.blit(player_img, (position[0], position[1]))
            pygame.display.update()
    