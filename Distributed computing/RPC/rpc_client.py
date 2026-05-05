import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input
num = int(input("Enter a number: "))

# Call remote function
result = client.factorial(num)

# Print result
print("Factorial =", result)
