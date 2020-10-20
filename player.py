dicionario_direction = {
    0: (0, -10), 1: (10, -10), 2: (10, 0), 3: (10, 10), 4: (0, 10), 5: (-10, 10), 6: (-10, 0), 7: (-10, -10)
}

class Player:

    def __init__(self, position, direction):
        self.__position = [position[0], position[1]]
        self.__life = 3
        self.__arrow = True
        self.sprite_postion = [48, 48]
        self.__direction = direction

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

    def move(self, tuple_moviment):
        direcao = -1
        for key in dicionario_direction.keys():
            if dicionario_direction[key] == tuple_moviment:
                direcao = key
                break

        if(key != -1):
            self.__direction = key

        self.__position[0] += tuple_moviment[0]
        self.__position[1] += tuple_moviment[1]
        



    

    

    