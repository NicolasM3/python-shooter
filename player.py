
class Player:

    def __init__(self):
        self.position = [100, 100]
        self.life = 3
        self.arrow = True
        self.sprite_postion = [48, 48]

    #@property
    def getlife(self):
        return self.life

    #@life.setter
    def setlife(self, damage):
        self.life -= damage

    #@property
    def get_arrow(self):
        return self.arrow

    #@arrow.setter
    def defarrow(self, state):
        self.arrow = state 

    def move(self, tuple_moviment):
        self.position[0] += tuple_moviment[0]
        self.position[1] += tuple_moviment[1]

    def get_postion(self):
        return self.position



    

    

    