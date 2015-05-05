from dog import Dog
from mapper import DogMapper
import sys

print("Reading in dog data from mapper and printing...\n")
dogs = DogMapper.read()
for dog in dogs:
    dog.print()

print("\nEnter a new dog to add...\n")
print("Name: ", end="")
name = sys.stdin.readline()
print("Breed: ", end="")
breed = sys.stdin.readline()
print("Age: ", end="")
age = sys.stdin.readline()

DogMapper.create(Dog(name, breed, age))

print("\nReading in dog data from mapper after creation...\n")
dogs = DogMapper.read()
for dog in dogs:
    dog.print()
