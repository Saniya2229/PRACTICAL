from xmlrpc.server import SimpleXMLRPCServer

# Function to concatenate strings
def concatenate(str1, str2):
    return str1 + str2

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running...")

# Register function
server.register_function(concatenate, "concatenate")

# Start server
server.serve_forever()