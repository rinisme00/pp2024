# Exercise 4: Add an instance method to the PlayerCharacter class called save_compress(filename) to perform two tasks:
# - Save the data by calling the previously implemented method save(filename).
# - then use os.system() or subprocess.run() method to compress the output file with the zip command as follows: 
# zip output.zip <filename>

import os
import subprocess

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
    
    def save_compress(self, filename):
        self.save(filename)
        try:
            zip_filename = "output.zip"
            subprocess.run(["zip", zip_filename, filename], check=True)
            print(f"File {filename} compressed into {zip_filename}.")
        except Exception as e:
            print(f"An error occured while compressing file: {e}")

# Main
if __name__ == "__main__":
    reservation = Reservation(guest="Emmanuel Macron", paid=True, room="R408")

    reservation.greet()

    long_reservation = LongReservation(guest="Joe Biden", paid=True, room="R502", months=6)

    long_reservation.greet()

    long_reservation.save_compress("long_reservation.txt")