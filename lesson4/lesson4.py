a = float(input("Enter a temperature in degrees C: "))
F = a * 9/5 + 32
print(f"{a} degrees F = {F} degrees C")

b = float(input("Enter a temperature in degrees F: "))
C = (b - 32) * 5/9
print(f"{b} degrees C = {C} degrees F")


#2
amount = float(input("Enter the initial amount: "))
annualRate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
years = int(input("Enter the number of years: "))
for year in range(1, years + 1):
    amount += amount * annualRate
    print(f"year {year}: ${amount:.2f}")

#3
a = int(input("enter a positive integer: "))
print(f"factors of {a}:")
for i in range(1, a + 1):
    if a % i == 0:
        print(f"{i} is a factor of {a}")

#4
