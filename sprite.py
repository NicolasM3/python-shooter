class sprite:
    def __init__(self, player_number, direction):
        if(player_number == 1):
            self.path = "sprites//shotgun//"
            self.__rotate = False            
        else:
            self.path = "sprites//rifle//"
            self.__rotate = True

        self.direction = direction
        self.count = 0
        self.images = []        
        for i in range(16):
            nmr = str(i).zfill(2)
            img = self.path + f"Armature_run_{nmr}.png"
            self.images.append(img)

        self.images_shoot = 

    def move(self, direction):
        if(direction == 4 or direction == 0):
            pass
        elif(direction <= 3):
            self.rotate = False
        else:
            self.rotate = True

        self.count = self.count + 1
        if(self.count >= 16):
            self.count = 0

    def stop(self):
        self.count = 0

    @property
    def current_image(self):
        return self.images[self.count]

    @property
    def rotate(self):
        return self.__rotate

    @rotate.setter
    def rotate(self, state):
        self.__rotate = state
    