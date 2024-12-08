class Bird:
    def sound(self):
        print("Chirp chirp")

class Dog:
    def sound(self):
        print("Woof woof")

# Polymorphic function
def make_sound(animal):
    animal.sound()

# Using polymorphism
bird = Bird()
dog = Dog()

make_sound(bird)  
make_sound(dog)  
