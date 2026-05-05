import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("1. Book Room")
print("2. Cancel Room")

choice = int(input("Enter choice: "))
name = input("Enter name: ")

if choice == 1:
    print(client.book_room(name))
elif choice == 2:
    print(client.cancel_room(name))