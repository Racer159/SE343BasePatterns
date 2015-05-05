from abc import ABCMeta, abstractmethod

class Animal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def say_something(self):
        return "I'm an animal!"
