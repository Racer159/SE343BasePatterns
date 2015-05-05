from cat import Cat
from dog import Dog
import sys

print("Are you a dog lover? (y/n)", end='')
yn = sys.stdin.readline()
if yn == "y\n":
    print("Nice! High-five!")
    dog = Dog()
    print(dog.say_something())
else:
    print("Fine, I guess you'll like this...")
    cat = Cat()
    print(cat.say_something())
    
