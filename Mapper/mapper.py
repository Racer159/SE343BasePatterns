from dog import Dog

class DogMapper:
    def create(dog):
        file = open('dogs.data', 'a')
        csv = "\n" + dog.name.strip('\n') + "," + dog.breed.strip('\n') + "," + dog.age.strip('\n')
        file.write(csv)
        file.close()

    def read():
        dogs = []
        file = open('dogs.data', 'r')
        if file.readline() == "name,breed,age\n":
            for line in file:
                values = line.strip('\n').split(',')
                dogs.append(Dog(values[0], values[1], values[2]))
        file.close()
        
        return dogs
            
        
