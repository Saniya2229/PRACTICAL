# Fuzzy Sets
A = {'x1':0.2, 'x2':0.5, 'x3':0.8}
B = {'y1':0.6, 'y2':0.4, 'y3':0.7}

# Basic Operations
print("Union:", {k:max(A[k], list(B.values())[i]) for i,k in enumerate(A)})
print("Intersection:", {k:min(A[k], list(B.values())[i]) for i,k in enumerate(A)})
print("Complement of A:", {k:1-A[k] for k in A})
print("Difference (A-B):", {k:min(A[k], 1-list(B.values())[i]) for i,k in enumerate(A)})

# Cartesian Product (Relation R)
R = {(a,b):min(A[a], B[b]) for a in A for b in B}
print("\nRelation R:", R)

# Another Relation S
S = {('y1','z1'):0.3, ('y1','z2'):0.6,
     ('y2','z1'):0.5, ('y2','z2'):0.9,
     ('y3','z1'):0.4, ('y3','z2'):0.8}

# Max-Min Composition
C = {(x,z): max(min(R[(x,y)], S[(y,z)]) for y in B)
     for x in A for z in ['z1','z2']}

print("\nMax-Min Composition:", C)