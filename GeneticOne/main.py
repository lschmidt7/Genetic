from Population import Population

values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
population_size = 1000
chromosome_size = 16
cross_rate = 1.0
generations = 1000

def func(chromosome):
    i=0
    hit=0
    solution = "leonardo schmidt"
    for g in chromosome:
        if(g==solution[i]):
            hit+=1
        i+=1
    return hit

p = Population(population_size,chromosome_size,values,cross_rate,func)
p.init()
p.fitness()
for x in range(generations):
    print(p.population[0].chromosomo)
    p.crossover()
    if(p.population[0].fitness==chromosome_size):
        print("\nSOLUCAO")
        print(p.population[0].chromosomo)
        print("\n")
        break