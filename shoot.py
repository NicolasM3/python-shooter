dicionario_direction = {
    0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)
}

# state 0 = guardada, 1 = em movimento, 2 = no chao

class shoot:
    def __init__(self, direction, position, image_number):
        self.__state = 0

        self.__speed = 20
        self.__power = 40
        self.__direction = direction
        self.__position = position
        
        self.incremento_x = dicionario_direction[direction][0] * self.__speed
        self.incremento_y = dicionario_direction[direction][1] * self.__speed

        self.images = [
            f"arrow{image_number}_top.bmp",
            f"arrow{image_number}_top_right.bmp",
            f"arrow{image_number}_right.bmp",
            f"arrow{image_number}_down_right.bmp",
            f"arrow{image_number}_down.bmp",
            f"arrow{image_number}_down_left.bmp",
            f"arrow{image_number}_left.bmp",
            f"arrow{image_number}_top_left.bmp",
            f"arrow{image_number}_ground.bmp"
        ]

        
        self.__current_image = self.images[direction]

    def move(self):
        self.__position[0] += self.incremento_x
        self.__position[1] += self.incremento_y
        
        self.__power -= 1
        
        if(self.__power <= 0):
            self.__current_image = self.images[8]
            self.__state = 2

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

    @property
    def current_image(self):
        return self.__current_image

    @current_image.setter
    def current_image(self, direction):
        self.__current_image = self.images[direction]



