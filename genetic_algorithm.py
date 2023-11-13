'''
CSCI 411
Genetic Algorithm
Author: Daniel Hawkins
'''

import random

'''
Initializes a starting population
popSize - int - The desired size of the population
chromLen - int - The length of each chromosome
return - list[list[int]] - A list representing the population, where each
         entry is a list of bits (0 or 1)
'''
def initPopulation(popSize, chromLen):
    population = []
    for _ in range(popSize):
        chrom = []
        for _ in range(chromLen):
            bit = random.choice([0, 1])
            chrom.append(bit)
        population.append(chrom)
    return population

'''
Calculates the fitness of a given chromosome based on its sum
chrom - list[int] - A list of bits representing a chromosome
return - int - Sum of the chromosome's bits
'''
def fitness(chrom):
    return sum(chrom)

'''
Selects two parents from the top half of a sorted population
population - list[list[int]] - A sorted list representing the population
return - tuple(list[int], list[int]) - Two selected parent chromosomes
'''
def selectParents(population):
    if len(population) == 1:
        return population[0], population[0]
    elif len(population) == 2:
        return population[0], population[1]
    parent1 = random.choice(population[0:len(population)//2])
    parent2 = random.choice(population[0:len(population)//2])
    return parent1, parent2

'''
Performs single-point crossover between two parent chromosomes
parent1 - list[int] - The first parent chromosome
parent2 - list[int] - The second parent chromosome
return - tuple(list[int], list[int]) - Two child chromosomes resulting
                                       from the crossover.  
'''
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

'''
Mutates a given chromosome based on a mutation rate
chrom - list[int] - A list of bits representing a chromosome to be mutated
mutRate - float - The probability of each bit being mutated
return - list[int] - A new chromosome after mutation
'''
def mutate(chrom, mutRate):
    newChrom = []
    for i in range(len(chrom)):
        if random.random() > mutRate:
            newChrom.append(chrom[i])
        else:
            if chrom[i] == 0:
                newChrom.append(1)
            else:
                newChrom.append(0)
    return newChrom

'''
Implements a basic genetic algorithm to optimize the chromosome fitness
numGen - int - Number of generations the algorithm should run
popSize - int - Desired size of the population
chromLength - int - Length of each chromosome
mutRate - float - Mutation rate for each bit of a chromosome
return - list[int] - The best chromosome based on fitness after numGen
                     generations.    
'''
def geneticAlgo(numGen, popSize, chromLen, mutRate):
    population = initPopulation(popSize, chromLen)
    for gen in range(numGen):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == chromLen:
            return population[0], gen + 1
        newPop = []
        while len(newPop) < popSize:
            parent1, parent2 = selectParents(population)
            child1, child2 = crossover(parent1, parent2)
            newPop += [mutate(child1, mutRate), mutate(child2, mutRate)]
        population = newPop
    return max(population, key=fitness), numGen

numGen = 100
popSize = 50
chromLength = 10
mutRate = 0.01

bestChrom, gensTaken = geneticAlgo(numGen, popSize, chromLength, mutRate)
print(f"Best chromosome: {bestChrom}")
print(f"Fitness: {fitness(bestChrom)}")
print(f"Generations taken: {gensTaken}")