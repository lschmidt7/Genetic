from Population import Population
from Imagem import Imagem
from Filters import Filters
import MathT
import pygame

pygame.init()
screen = pygame.display.set_mode((256, 256))
done = False


values = 255
cross_rate = 1.0
population_size = 50 # triangles per image
chromosome_size = 9*50
mutation_rate = 0.05
generations = 10000

f = Filters()

img = Imagem()
img.open("../Imagens/monalisa.jpg")
img.load()
pixels = img.vectorize()
pixeis = []
for x in pixels:
    for y in x:
        pixeis.append(y)

def func(chromosome,solution):
    hit=0
    for x in range(256):
        for y in range(256):
            p=[x,y]
            a=chromosome[0:2]
            b=chromosome[2:4]
            c=chromosome[4:6]
            if(MathT.PointInTriangle(p,a,b,c) and solution[p[0]*256+y+6:p[0]*256+y+9] == chromosome[6:9]):
                hit+=1
    return hit

p=Population(population_size,chromosome_size,values,cross_rate,mutation_rate,func,pixeis)
p.init()
p.fitness()

for x in range(generations):
    p.crossover()
    p.mutation()
    chrom = p.population[0].chromosomo
    for x in range(int(chromosome_size/9)):
        color = chrom[x*9+6:x*9+9]
        print(color)
        color = color.extend([255])
        print(color)
        coords = [[chrom[x*9+0],chrom[x*9+1]],[chrom[x*9+2],chrom[x*9+3]],[chrom[x*9+4],chrom[x*9+5]]]
        pygame.draw.polygon(screen, color, coords, 1)
    pygame.display.flip()
    if(p.population[0].fitness>(0.7*(256*256))):
        print("solution")
        break
        
        