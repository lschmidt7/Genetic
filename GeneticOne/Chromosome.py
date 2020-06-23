import random

class Chromosome():

    def __init__(self,size):
        self.chromosomo = [0]*size
        self.fitness = 0
        self.limit = 0
    
    def randomize(self,values):
        for x in range(len(self.chromosomo)):
            self.chromosomo[x] = values[random.randint(0,len(values)-1)]