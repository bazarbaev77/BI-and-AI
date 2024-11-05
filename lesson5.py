class Car:
    def __init__(self, year, make):
        self.year = year
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

car = Car(2022, "Chevy")

print("Accelerating the car:")
for i in range(5):
    car.accelerate()
    print(f"Current speed: {car.speed} km")

print("\nBraking the car:")
for i in range(5):
    car.brake()
    print(f"Current speed: {car.speed} km")


#2
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "cow")

    def speak(self):
        print(f"{self.name} says 'Moo!'")

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "chicken")

    def speak(self):
        print(f"{self.name} says 'Cluck!'")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")

    def speak(self):
        print(f"{self.name} says 'Gav Gav!'")

Mbape = Cow("Mbape")
Messi = Chicken("Messi")
Benzeman = Dog("Benzeman")

Mbape.eat()
Mbape.speak()

Messi.eat()
Messi.speak()

Benzeman.eat()
Benzeman.speak()

