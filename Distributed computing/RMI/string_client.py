import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Call remote method
result = client.concatenate(s1, s2)

# Print result
print("Concatenated String:", result)