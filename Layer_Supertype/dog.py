from animalsuper import Animal

class Dog(Animal):
    def say_something(self):
        s = super(Dog, self).say_something()
        return "%s - %s" % (s, "Woof!")
