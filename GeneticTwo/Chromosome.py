import random

class Chromosome():

    def __init__(self,size):
        self.size = size
        self.chromosomo = [0]*size
        self.fitness = 0
        self.limit = 0
    
    def randomize(self,values):
        for x in range(int(self.size/9)):
            for y in range(6):
                self.chromosomo[x*9+y] = random.randint(0,values)
            for y in range(3):
                self.chromosomo[x*9+6+y] = list(range(0,256))[random.randint(0,255)]