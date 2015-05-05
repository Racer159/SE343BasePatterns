from dog import Dog
from servicestub import DogServiceStub

service = DogServiceStub()

dogs = service.get_dogs()

for dog in dogs:
    dog.print()
