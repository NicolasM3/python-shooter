dicionario_direction = {
    0: [0, -3], 1: [3, -3], 2: [3, 0], 3: [3, 3], 4: [0, 3], 5: [-3, 3], 6: [-3, 0], 7: [-3, -3]
}

# state 0 = guardada, 1 = em movimento, 2 - no chao

class shoot:
    def __init__(self, direction, position):
        self.__state = 0
        self.__direction = direction
        self.__position = position
        self.__target_position = position
        self.incremento_x = dicionario_direction[direction][0]
        self.incremento_y = dicionario_direction[direction][1]


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
    def position_x(self, state):
        self.__position = state

    @property
    def target_position(self):
        return self.__target_position
    
    @target_position.setter
    def target_position(self, position):
        self.__target_position = position

    def move(self):
        self.__position[0] += self.incremento_x
        self.__position[1] += self.incremento_y
        if(self.__target_position[0] <= self.__position[0] <= self.__target_position[0] + 48):
            if(self.__target_position[1] <= self.__position[1] <= self.__target_position[1] + 48):
                self.__state = 2

