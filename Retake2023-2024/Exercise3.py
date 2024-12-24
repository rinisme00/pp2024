# Exercise 3: Add an instance method to LongReservation class called save(filename) to save information of the current 
# reservation to a text file filename. Each piece of information should be written on a seperated line. The save() method 
# should handle exeption properly, just in case there is some errors at runtime happened


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
    
    def save(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write(f"Guest: {self.guest}\n")
                file.write(f"Paid: {self.paid}\n")
                file.write(f"Room: {self.room}\n")
                file.write(f"Months: {self.months}\n")
            print(f"Reservation details saved to {filename}.")
        except Exception as e:
            print(f"An error occured while saving reservation details: {e}")

# Main
if __name__ == "__main__":
    reservation = Reservation(guest="Emmanuel Macron", paid=True, room="R408")

    reservation.greet()

    long_reservation = LongReservation(guest="Joe Biden", paid=True, room="R502", months=6)

    long_reservation.greet()

    long_reservation.save("long_reservation.txt")