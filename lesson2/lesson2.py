a = float(input("Please enter the number: "))
rounded_number = round(a, 2)
print(f"Rounded number: {a}")

#2
P = int(input("Please enter the number 1: "))
D = int(input("Please enter the numbers 2: "))
C = int(input("Please enter the numbers 3: "))

f = max(P, D, C)
print(f"Max number: {f}")

#3
km = float(input("Enter the amount of km: "))

m = km * 1000
cm = km * 100000

print(f"{km} kilometers is {m} meters and {cm} centimeters.")

#4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

q = num1 // num2
r = num1 % num2

print(f"The result of integer division is: {q}")
print(f"The remainder is: {r}")

#5
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}C is equal to {fahrenheit}F")

#6
d = input("enter the number: ")
f = (d[-1])
print(f"{f} is the last number")

#7
l = input("Enter the number: ")

if l % 2 == 0:
    print(f"{l} is even.")
else:
    print(f"{l} is odd.")

#8
a = input("Enter a: ")
b = input("Enter b: ")

a, b = b, a

print("After:")
print("a =", a)
print("b =", b)


#String datatype

#1
text = input("Enter the text: ")
capitalized_text = text.upper()
print(f"Capitalized version: {capitalized_text}")

#2
text = input("Enter teh text: ")

for vowel in "aeiouAEIOU":
    text = text.replace(vowel, "")

print("Text without vowels:", text)

#3
text = input("Enter the text: ")
rt = text[::-1]
print(f"Reversed version: {rt}")

#4
text = input("Enter teh text: ")

for b in " ":
    text = text.replace(b, "_")
print(text)

#5
word = input("Enter the etxt: ")

cleaned_word = word.replace(" ", "").lower()

if cleaned_word == cleaned_word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

#6
text = input("Enter teh text: ")

for b in "a":
    text = text.replace(b, "o")
print(text)

#7
email = input("Enter your email: ")

un = email.split('@')[0]

print("Username:", un)

#8
text = input("Enter the string: ")

title = text.title()

print("Output:", title)

#9
text = input("Enter the text: ")

title = text[1:-1]

print("Output:", title)

#10
text = input("Enter the sentence: ")
word = input("Enter the word: ")
if word in text:
    print("It is in the text")
else:
    print("It is not in the text")

#11
text = input("Enter the text: ")

find = input("Enter a character to find: ")

position = text.find(find)

if position != -1:
    print(f"The first occurrence of '{find}' is at position: {position}")
else:
    print(f"'{find}' is not found in the string.")

#12
string = "hello"
print(string[-3:])

#13
text, times = "hello", 3
print(text * times)  

# 14
s = "This is a test"
for word in s.split():
    print(word)  

# 15
str = "hello"
print(str[1::2])

# 16
str = "<String>"
print(f"Title: {str}")

# 17
sentence = "hello world"
print(sentence[::-1])

# 18
string1, string2 = "hello", "world!"
print((len(string1) - len(string2)))


#The boolean datatypes 
#1
username = input("Enter username: ")
password = input("Enter password: ")
print("Both are not empty:", bool(username) and bool(password))

# 2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Equal" if num1 == num2 else "Not equal.")

# 3
number = int(input("Enter a number: "))
print("The number is positive and even:", number > 0 and number % 2 == 0)

# 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("All numbers are different:", num1 != num2 and num1 != num3 and num2 != num3)

# 5
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print("Same length:", len(string1) == len(string2))

# 6
number = int(input("Enter a number: "))
print("Divisible by both 3 and 5:", number % 3 == 0 and number % 5 == 0)


# 7
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum > 50:", (num1 + num2) > 50)


# 8
number = int(input("Enter a number: "))
print("Between 10 and 20:", 10 <= number <= 20)

key = (1,2,3)
for k in key:
    print(k**2)