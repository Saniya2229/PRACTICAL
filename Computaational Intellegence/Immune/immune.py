import random

# Sample data: (feature, label) 1 = Damaged, 0 = Normal
data = [(10,1), (20,1), (5,0), (3,0), (15,1)]

# Generate detectors (antibodies)
detectors = [random.randint(1, 20) for _ in range(3)]

print("Detectors:", detectors)

# Classification
def classify(x):
    for d in detectors:
        if abs(x - d) < 3:   # matching rule
            return "Damaged"
    return "Normal"

# Test data
test = [4, 12, 18]

for t in test:
    print("Value:", t, "->", classify(t))