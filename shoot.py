dicionario_direction = {
    0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)
}

# state 0 = guardada, 1 = em movimento, 2 - no chao

class shoot:
    def __init__(self, direction, position):
        self.__speed = 20
        self.__power = 200
        self.__state = 0
        self.__direction = direction
        self.__position = position
        self.incremento_x = dicionario_direction[direction][0] * self.__speed
        self.incremento_y = dicionario_direction[direction][1] * self.__speed


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
    
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

    def move(self):
        self.__position[0] += self.incremento_x
        self.__position[1] += self.incremento_y
        self.__power -= 1
        
        if(self.__power <= 0):
            self.__state = 2
