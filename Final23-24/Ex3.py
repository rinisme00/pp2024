"""
Add an instance method to the PlayerCharacter class called save(filename) to save information of the current character to a text file
filename. Each piece of information should be wriiten on a seperated line. The save() method should handle exception properly, just in
case there is some error at runtime happened.
"""
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
    
if __name__ == "__main__":
    character1 = PlayerCharacter(name = "Stone Giant", level = 1, health = 780, inventory = ["Sword", "Shield"])
    print(character1)
    character1.save("player1_data.txt")