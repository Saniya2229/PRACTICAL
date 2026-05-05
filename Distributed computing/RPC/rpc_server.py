from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Invalid Input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running...")

# Register function
server.register_function(factorial, "factorial")

# Start server
server.serve_forever()