# Exercise 1: Define a Python class called Reservation to manage reservations of a hotel
# - guest: The guest's name
# - paid: Payment status of the reservation.
# - room: The room of the stay.
# Implement a constructor (__init__) that initializes these attributes with given values. Also, create a method called 
# greet() that prints a greeting message with the guest's name and the room name. Create an instance of the Reservation 
# class with the following details:
# - guest: "Emmanuel Macron"
# - paid: True
# - room: "R408"

# Reservation class
class Reservation:
    def __init__(self, guest, paid, room):
        self.guest = guest
        self.paid = paid
        self.room = room

    def greet(self):
        print(f"Welcome, {self.guest}! Your room number is {self.room}.")

# Main
if __name__ == "__main__":
    reservation = Reservation(guest="Emmanuel Macron", paid=True, room="R408")

    reservation.greet()
