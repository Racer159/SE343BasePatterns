class Dog:
	name = ""
	breed = ""
	age = 0
	
	def __init__(self, name, breed, age):
		self.name = name
		self.age = age
		self.breed = breed

	def print(self):
                print("Hi, I'm a " + self.breed + " named " + self.name +
                      " and am " + self.age + " years old.")
