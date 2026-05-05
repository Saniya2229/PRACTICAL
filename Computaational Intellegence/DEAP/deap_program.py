from deap import base, creator, tools
import random

creator.create("F", base.Fitness, weights=(1.0,))
creator.create("I", list, fitness=creator.F)

t = base.Toolbox()
t.register("bit", random.randint, 0, 1)
t.register("ind", tools.initRepeat, creator.I, t.bit, 5)
t.register("eval", lambda x: (sum(x),))

pop = [t.ind() for _ in range(5)]

for _ in range(5):
    for i in pop: i.fitness.values = t.eval(i)
    pop = tools.selTournament(pop, 5, 3)

    for i in range(0, 4, 2):
        tools.cxTwoPoint(pop[i], pop[i+1])
        tools.mutFlipBit(pop[i], 0.2)

best = tools.selBest(pop, 1)[0]
print("Best:", best, "Fitness:", sum(best))