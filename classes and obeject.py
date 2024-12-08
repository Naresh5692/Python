# Define a class
class Animal:
    def __init__(self, name, species):
        self.name = name  # Instance variable
        self.species = species  # Instance variable

    def display_info(self):  # Method
        print(f"{self.name} is a {self.species}")

# Create an object
dog = Animal("Buddy", "Dog")

# Call a method
dog.display_info()
