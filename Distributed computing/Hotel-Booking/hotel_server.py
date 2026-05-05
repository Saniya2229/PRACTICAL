from xmlrpc.server import SimpleXMLRPCServer

bookings = []

# Book room
def book_room(name):
    bookings.append(name)
    return f"Room booked for {name}"

# Cancel booking
def cancel_room(name):
    if name in bookings:
        bookings.remove(name)
        return f"Booking cancelled for {name}"
    else:
        return "No booking found"

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server running...")

server.register_function(book_room, "book_room")
server.register_function(cancel_room, "cancel_room")

server.serve_forever()