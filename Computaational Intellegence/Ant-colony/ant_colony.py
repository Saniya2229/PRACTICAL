import random

dist = [
    [0, 2, 3, 4],
    [2, 0, 5, 6],
    [3, 5, 0, 7],
    [4, 6, 7, 0]
]

def cost(path):
    return sum(dist[path[i]][path[i+1]] for i in range(len(path)-1)) + dist[path[-1]][path[0]]

paths = [random.sample(range(4), 4) for _ in range(10)]
best = min(paths, key=cost)

print("Best Path:", best)
print("Min Cost:", cost(best))