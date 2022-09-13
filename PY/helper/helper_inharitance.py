


class Mammal:
    blood_temp = 'warm'
    def identify(self):
        print("I'm a mammal!")

class Dog(Mammal):
    species = 'canine'
    def greet(self):
        print("Hi, I'm a ", self.species)
        self.identify()


dog = Dog()
dog.greet()


