from dog import Dog
from dogservice import DogService

class DogServiceStub:
    def get_dogs(self):
        dogs = [Dog("Betsy","Husky",4), Dog("Tex","Dingo",5)]
        return dogs
