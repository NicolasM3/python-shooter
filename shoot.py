dicionario_direction = {
    0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)
}

# state 0 = guardada, 1 = em movimento, 2 = no chao

# classe que representa o tiro
class shoot:
    # definimos as variaveis direcao, posicao, nmr da imagem, velocidade e força
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

    # função para mover o tiro de acordo com o incremento
    def move(self):
        # incrementa-se a posiçao x e y
        self.__position[0] += self.incremento_x
        self.__position[1] += self.incremento_y
        
        # diminui-se 1 na força
        self.__power -= 1
        
        # se a força é 0, paramos a flecha
        if(self.__power <= 0):
            self.__current_image = self.images[8] # coloca-se a imagem da flecha caída
            self.__state = 2                      # mudamos o estado para a flecha no chao

    # getter para o estado
    @property
    def state(self):
        return self.__state

    # setter para o estado
    @state.setter
    def state(self, state):
        if(state == 2):
            self.__current_image = self.images[8]
        self.__state = state
    
    # getter para a direcao
    @property
    def direction(self):
        return self.__direction

    # setter para a direcao
    @direction.setter
    def direction(self, state):
        self.__direction = state

    # getter para a posicao
    @property
    def position(self):
        return self.__position

    # setter para a posição
    @position.setter
    def position(self, state):
        self.__position = state

    # getter para a imagem atual
    @property
    def current_image(self):
        return self.__current_image

    # setter para a imagem atual
    @current_image.setter
    def current_image(self, direction):
        self.__current_image = self.images[direction]



