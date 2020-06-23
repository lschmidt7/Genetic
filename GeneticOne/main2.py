from Population import Population
from Imagem import Imagem
from Filters import Filters

f = Filters()

img = Imagem()
img.open("Imagens/monalisa.jpg")
img.greyScale()
img.load()
matrix = f.binary(img.toMatrix(),100)
img.setMatrix(matrix)
img.save("Imagens/monalisagrey.jpg")
solve = img.vectorize()

values = [0,255]
population_size = 100
chromosome_size = 8
cross_rate = 1.0
mutation_rate = 0.05
generations = 10000

times = int(65536/chromosome_size)

def func(chromosome,solution):
    i=0
    hit=0
    for g in chromosome:
        if(g==solution[i]):
            hit+=1
        i+=1
    return hit

comunity = []
ini = 0
for x in range(times):
    p=Population(population_size,chromosome_size,values,cross_rate,mutation_rate,func,solve[ini:ini+chromosome_size])
    p.init()
    p.fitness()
    comunity.append(p)
    ini+=chromosome_size

for x in range(generations):
    img2 = Imagem()
    img2.new(256,256)
    img2.load()
    vector = []
    for y in range(times):
        vector.extend(comunity[y].population[0].chromosomo)
    img2.vectorToMatrix(vector)
    nome = "000000000"+str(x)+".jpg"
    img2.save("Imagens/gen"+nome[len(nome)-10:len(nome)])
    for y in range(times):
        comunity[y].crossover()
    for y in range(times):
        comunity[y].mutation()
    soma = 0
    for y in range(times):
        soma += comunity[y].population[0].fitness
    print((soma/65536.0)*100.0)
    if(soma>(65536*0.9999)):
        print("\nSOLUCAO")
        print("\n")
        break