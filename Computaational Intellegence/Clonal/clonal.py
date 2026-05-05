import random

# Fitness function (maximize value)
def fitness(x):
    return x * x

# Initial population
population = [random.randint(1, 10) for _ in range(5)]

for generation in range(5):
    print("\nGeneration", generation+1)

    # Evaluate fitness
    population.sort(key=fitness, reverse=True)
    print("Population:", population)

    # Select best 2
    selected = population[:2]

    # Clone (duplicate)
    clones = selected * 2

    # Mutation (small change)
    mutated = [x + random.randint(-1,1) for x in clones]

    # New population
    population = mutated

# Best solution
best = max(population, key=fitness)
print("\nBest Solution:", best, "Fitness:", fitness(best))