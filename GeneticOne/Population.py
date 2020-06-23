from Chromosome import Chromosome
import random

class Population():

    def __init__(self,size_population,size_chromosome,values,cross_rate,mutation_rate,func,solution):
        self.size_population = size_population
        self.size_chromosome = size_chromosome
        self.values = values
        self.func = func
        self.solution = solution
        self.population = []
        self.mutation_rate = mutation_rate
    
    def init(self):
        for x in range(self.size_population):
            c = Chromosome(self.size_chromosome)
            c.randomize(self.values)
            self.population.append(c)
    
    def getKey(self,item):
        return item.fitness

    def order(self,vector):
        return sorted(vector, key=self.getKey,reverse=True)

    def show(self):
        for x in self.population:
            print(x.fitness)
    
    def fitness(self):
        for x in self.population:
            x.fitness = self.func(x.chromosomo,self.solution)
        
    def roulette(self,comunity,sorted_value):
        total = 0
        for x in comunity:
            total+=x.fitness
        comunity = self.order(comunity)
        aux = 0
        if(total==0):
            return comunity[0]
        for x in comunity:
            x.limit = x.fitness/total + aux
            aux+=x.limit
            if(sorted_value<x.limit):
                return x
    
    def crossover(self):
        comunity = self.population
        for x in range(int(len(comunity)/2)):
            sorting = random.uniform(0.0,1.0)
            cromosome1 = self.roulette(comunity,sorting)
            comunity.remove(cromosome1)
            sorting = random.uniform(0.0,1.0)
            cromosome2 = self.roulette(comunity,sorting)
            comunity.remove(cromosome2)
            point = random.randint(1,self.size_chromosome-1) # CUIDADO
            child_one = Chromosome(self.size_chromosome)
            child_two = Chromosome(self.size_chromosome)
            child_one.chromosomo = cromosome1.chromosomo[0:point]+cromosome2.chromosomo[point:self.size_chromosome]
            child_two.chromosomo = cromosome2.chromosomo[0:point]+cromosome1.chromosomo[point:self.size_chromosome]
            self.population.append(child_one)
            self.population.append(child_two)
        self.fitness()
        self.population = self.order(self.population)
        self.population = self.population[0:self.size_population]
    
    def mutation(self):
        for x in range(len(self.population)):
            sorting = random.uniform(0.0,1.0)
            if(sorting<=self.mutation_rate):
                index = random.randint(0,self.size_chromosome-1)
                if(self.population[x].chromosomo[index]==0):
                    self.population[x].chromosomo[index]=255
                else:
                    self.population[x].chromosomo[index]=0