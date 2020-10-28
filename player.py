from shoot import shoot

dicionario_direction = {
    0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)
}

class Player:

    def __init__(self, position, direction):
        
        self.__position = [position[0], position[1]]
        self.__speed = 10
        self.__life = 3
        self.__arrow = shoot(direction, [position[0], position[1]])
        self.sprite_postion = [48, 48]
        self.__direction = direction

    def move(self, tuple_moviment):
        for key in dicionario_direction:
            if dicionario_direction[key] == tuple_moviment:
                self.__direction = key
                break

        self.__position[0] += tuple_moviment[0] * self.__speed
        self.__position[1] += tuple_moviment[1] * self.__speed
        
    def shoot(self):
        self.__arrow = shoot(self.__direction, [self.__position[0], self.__position[1]])
        self.__arrow.state = 1

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




    

    

    