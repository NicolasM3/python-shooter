
class Player:

    def __init__(self):
        self.position = [100, 100]
        self.__life = 3
        self.__arrow = True
        self.sprite_postion = [48, 48]

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

    def move(self, tuple_moviment):
        self.position[0] += tuple_moviment[0]
        self.position[1] += tuple_moviment[1]

    def get_postion(self):
        return self.position



    

    

    