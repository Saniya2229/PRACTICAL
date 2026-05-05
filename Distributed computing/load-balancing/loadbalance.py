# Server class
class Server:
    def __init__(self, name):
        self.name = name
        self.load = 0   # number of requests

# Create servers
servers = [Server("S1"), Server("S2"), Server("S3")]

# Client requests
requests = ["R1", "R2", "R3", "R4", "R5"]

# -------- Round Robin --------
print("Round Robin:")

index = 0
for r in requests:
    server = servers[index]
    print(r, "->", server.name)
    
    index = (index + 1) % len(servers)

# -------- Least Connections --------
print("\nLeast Connections:")

for r in requests:
    # select server with minimum load
    server = min(servers, key=lambda s: s.load)
    
    print(r, "->", server.name)
    
    server.load += 1   # increase load