from dog import Dog
from abc import ABCMeta, abstractmethod

class DogService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_dogs(self):
        raise Exception("NotImplementedException")
