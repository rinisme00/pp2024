"""
Create a Python class called Character for a game with the following attributes:
- name: representing the character's name
- level: representing the chracter's experience level (e.g. 1, 2, 3)
- health: representing the chracter's health points (HP)

Create an instance of the Character class with the following details:
- Name: Stone Giant
- Level: 1
- Health: 780
"""

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

if __name__ == "__main__":
    character1 = Character(name = "Stone Giant", level = 1, health = 780)