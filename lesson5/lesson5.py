import random
import os
from collections import Counter


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


#  EXCEPTION HANDLING
try:
    num = 10
    result = num / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


#2
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That is not a valid integer!")

#3
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist!")

#4
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = float(num1) + float(num2)
except ValueError:
    print("Both inputs must be numerical!")


#5
try:
    with open("protected_file.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("You do not have permission to access this file!")


#6
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index is out of range!")


#7
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput interrupted by user!")


#8
try:
    result = 10 / 0
except ArithmeticError:
    print("An arithmetic error occurred!")


#9
try:
    with open("non_utf_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
except UnicodeDecodeError:
    print("There was an encoding issue with the file!")

#10
my_list = [1, 2, 3]
try:
    my_list.append("new_element")
    my_list.add("another_element")  
except AttributeError:
    print("The list does not have the 'add' method!")



#FILE HANDLING EXERCISES

# 1
with open('file.txt', 'r') as file:
    content = file.read()
    print("Entire file content:")
    print(content)

# 2
n = int(input("\nEnter the number of first lines to read: "))
with open('file.txt', 'r') as file:
    for i in range(n):
        print(file.readline(), end='')

# 3
text_to_append = "This is the appended text."
with open('file.txt', 'a') as file:
    file.write(text_to_append + '\n')

with open('file.txt', 'r') as file:
    print("\nFile content after appending:")
    print(file.read())

# 4
n = int(input("\nEnter the number of last lines to read: "))
with open('file.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end='')

# 5
with open('file.txt', 'r') as file:
    lines = file.readlines()
print("\nList of lines:")
print(lines)

# 6
content = ''
with open('file.txt', 'r') as file:
    for line in file:
        content += line
print("\nFile content stored in variable:")
print(content)

# 7
lines_array = []
with open('file.txt', 'r') as file:
    for line in file:
        lines_array.append(line.strip())
print("\nArray of lines:")
print(lines_array)

# 8
with open('file.txt', 'r') as file:
    words = file.read().split()
longest_word = max(words, key=len)
print("\nThe longest word is:", longest_word)

# 9
with open('file.txt', 'r') as file:
    line_count = sum(1 for line in file)
print("\nNumber of lines:", line_count)

# 10
with open('file.txt', 'r') as file:
    words = file.read().split()
word_counts = Counter(words)
print("\nWord frequency count:")
print(word_counts)

# 11
file_size = os.path.getsize('file.txt')
print(f"\nFile size: {file_size} bytes")

# 12
my_list = ['apple', 'banana', 'cherry']
with open('file.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')

with open('file.txt', 'r') as file:
    print("\nContent after writing a list to file:")
    print(file.read())

# 13
with open('source_file.txt', 'r') as source_file:
    content = source_file.read()

with open('destination_file.txt', 'w') as destination_file:
    destination_file.write(content)

print("\nContents copied to 'destination_file.txt'.")

# 16
with open('file.txt', 'r') as file:
    print("\nFile closed:", file.closed)

# 17
with open('file.txt', 'r') as file:
    lines = file.readlines()

with open('file.txt', 'w') as file:
    for line in lines:
        file.write(line.strip() + '\n')

print("\nNewline characters removed from the file.")