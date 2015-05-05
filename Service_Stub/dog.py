class Dog:
    name = ""
    breed = ""
    age = 0

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def print(self):
        print("Hi, I'm a " + self.breed + " named " + self.name +
            " and am " + str(self.age) + " years old.")
