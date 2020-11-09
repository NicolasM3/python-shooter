from shoot import shoot
from sprite import sprite
import pygame

# Dicionário de direções
# cada chave apresenta uma tupla com o movimento x, y
# 0 - não movimenta
# 1 - movimenta
dicionario_direction = {
    0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)
}

class Player:

    # Construtor
    # player_number - Qual player é
    # position - Posição inicial do palyer
    # direction - Direção inicial do player
    def __init__(self, player_number, position, direction):
        self.__position = [position[0], position[1]]
        self.__speed = 10
        self.tick_shoot = 0                                                         # Gambiarra para fazer animação
        self.__life = 3
        self.player_number = player_number                                          # Se é o primeiro ou segundo player
        self.__arrow = shoot(direction, [position[0], position[1]], player_number)  # Flecha do player
        self.__sprite = sprite(player_number, direction)                            # Sprites do player
        self.__direction = direction


    # Método responsável pelo movimento
    # tuple_moviment - direções de movimentação do player
    # tela - tela a ser desenhada
    def move(self, tuple_moviment, tela):
        self.__position[0] += tuple_moviment[0] * self.__speed                      # Soma a direção * speed (0 ou 1 * 10)
        self.__position[1] += tuple_moviment[1] * self.__speed

        # Faz a animação de atirar
        if(self.tick_shoot != 0):
            self.__sprite.shoot(self.__direction, self.__position, tela, False)
            self.tick_shoot = self.tick_shoot - 1
            return

        # Redefine a direção com base na tupla enviada
        for key in dicionario_direction:                                                             
            if dicionario_direction[key] == tuple_moviment: 
                self.__direction = key
                break

        self.__sprite.move(self.direction, self.position, tela)                     # Chama o método de animar sprite


    # Chama a animação idle do personagem
    # tela - tela onde vai ser desenhado
    def idle(self, tela):   

        # Redefine a direção com base na tupla enviada                                                        
        if(self.tick_shoot != 0):
            self.__sprite.shoot(self.__direction, self.__position, tela, False)
            self.tick_shoot = self.tick_shoot - 1
            return
        self.sprite.stop(self.__position, tela)                                     # Chama o método de chamar a animação idle
        
    # Inicia uma nova arrow com as direções e faz as animações 
    # tela - tela onde será desenhada
    def shoot(self, tela):

        # instancia uma nova flecha
        self.__arrow = shoot(self.__direction, [self.__position[0], self.__position[1]], self.player_number)
        self.__arrow.state = 1

        # Instancia uma instancia de sprite para fazer as animações
        self.sprite.shoot(self.__direction, self.__position, tela, True)
        self.tick_shoot = 8

    # getters e setters
    @property
    def life(self):
        return self.__life
    @life.setter
    def life(self, damage):
        self.__life -= damage

    @property
    def arrow(self):
        return self.__arrow
    @arrow.setter
    def arrow(self, state):
        self.__arrow = state 

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, state):
        self.__direction = state

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, state):
        self.__position = state

    @property
    def sprite(self):
        return self.__sprite



    

    

    