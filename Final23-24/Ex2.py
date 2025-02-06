"""
Define a subclass called PlayerCharacter inheriting from the Character class. Add an additional attribute:
- inventory: representing the items the player character carries.
Override the __str__() method in the PlayerCharacter class to display information about the player character, including their name,
level, health, and inventory
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

if __name__ == "__main__":
    character1 = PlayerCharacter(name = "Stone Giant", level = 1, health = 780, inventory = ["Sword", "Shield"])
    print(character1)