from animalsuper import Animal

class Cat(Animal):
    def say_something(self):
        s = super(Cat, self).say_something()
        return "%s - %s" % (s, "Meow!")
