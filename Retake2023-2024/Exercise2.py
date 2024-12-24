# Exercise 2: Create a subclass called LongReservation that inherits from the Reservation class. The LongReservation class 
# should have an additional attribute:
# - months: The number of months that the reservation will take place.
# Override the greet() method to include the duration in the greeting

# Reservation class
class Reservation:
    def __init__(self, guest, paid, room):
        self.guest = guest
        self.paid = paid
        self.room = room

    def greet(self):
        print(f"Welcome, {self.guest}! Your room number is {self.room}.")

# LongReservation subclass
class LongReservation(Reservation):
    def __init__(self, guest, paid, room, months):
        super().__init__(guest, paid, room)
        self.months = months

    def greet(self):
        print(f"Welcome, {self.guest}! Your room number is {self.room}. You will be staying for {self.months} months.")

# Main
if __name__ == "__main__":
    reservation = Reservation(guest="Emmanuel Macron", paid=True, room="R408")

    reservation.greet()

    long_reservation = LongReservation(guest="Joe Biden", paid=True, room="R502", months=6)

    long_reservation.greet()