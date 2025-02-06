"""
Add an instance method to the PlayerCharacter class called save_in_background(filename) to create a seperated thread, in which calls
the previously defined method save(filename)

In the main thread, call the save_in_background() method to save information to file named "player.txt"
"""
import threading

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

class PlayerCharacter(Character):
    def __init__(self, name, level, health, inventory):
        super().__init__(name, level, health)
        self.inventory = inventory

    def __str__(self):
        inventory_str = ", ".join(self.inventory)
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nInventory: {inventory_str}"
    
    def save(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write(f"Name: {self.name}\n")
                file.write(f"Level: {self.level}\n")
                file.write(f"Health: {self.health}\n")
                file.write(f"Inventory: {', '.join(self.inventory)}\n")
            print(f"Player's data saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the data: {e}")
    
    def save_in_background(self, filename):
        background_thread = threading.Thread(target = self.save, args = (filename,))
        background_thread.start()

if __name__ == "__main__":
    character1 = PlayerCharacter(name = "Stone Giant", level = 1, health = 780, inventory = ["Sword", "Shield"])
    print(character1)
    character1.save_in_background("player.txt")