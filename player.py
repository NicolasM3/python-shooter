from shoot import shoot
from sprite import sprite
import pygame

dicionario_direction = {
    0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)
}

class Player:
    def __init__(self, player_number, position, direction):
        self.__position = [position[0], position[1]]
        self.__speed = 10
        self.tick_shoot = 0
        self.__life = 3
        self.player_number = player_number
        self.__arrow = shoot(direction, [position[0], position[1]], player_number)
        self.__sprite = sprite(player_number, direction)
        self.__direction = direction

    def move(self, tuple_moviment, tela):
        self.__position[0] += tuple_moviment[0] * self.__speed
        self.__position[1] += tuple_moviment[1] * self.__speed

        if(self.tick_shoot != 0):
            self.__sprite.shoot(self.__direction, self.__position, tela, False)
            self.tick_shoot = self.tick_shoot - 1
            return

        for key in dicionario_direction:
            if dicionario_direction[key] == tuple_moviment:
                self.__direction = key
                break

        self.__sprite.move(self.direction, self.position, tela)


    def idle(self, tela):
        if(self.tick_shoot != 0):
            self.__sprite.shoot(self.__direction, self.__position, tela, False)
            self.tick_shoot = self.tick_shoot - 1
            return
        self.sprite.stop(self.__position, tela)
        
    def shoot(self, tela):
        self.__arrow = shoot(self.__direction, [self.__position[0], self.__position[1]], self.player_number)
        self.__arrow.state = 1
        self.sprite.shoot(self.__direction, self.__position, tela, True)
        self.tick_shoot = 8

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



    

    

    