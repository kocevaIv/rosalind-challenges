def wascallyWabbits(n,k):
    rabbits_population=[1,1]
    for index in range(2,n):
        next_gen=rabbits_population[index-1]+rabbits_population[index-2]*k
        rabbits_population.append(next_gen)
    return rabbits_population
