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
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]



def enrollment_stats(data):
    enrollments = [uni[1] for uni in data]
    tuitions = [uni[2] for uni in data]
    return enrollments, tuitions



def mean(values):
    return sum(values) / len(values)



def median(values):
    sorted_val = sorted(values)
    n = len(sorted_val)
    mid = n // 2
    if n % 2 == 1:
        return sorted_val[mid]
    else:
        return (sorted_val[mid - 1] + sorted_val[mid]) / 2


if __name__ == "__main__":
    enrollments, tuitions = enrollment_stats(universities)
    total_students = sum(enrollments)
    total_tuition = sum(tuitions)
    student_mean = mean(enrollments)
    student_median = median(enrollments)
    tuition_mean = mean(tuitions)
    tuition_median = median(tuitions)

    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}")
    print(f"\nStudent mean: {student_mean:,.2f}")
    print(f"Student median: {student_median:,.0f}")
    print(f"\nTuition mean: $ {tuition_mean:,.2f}")
    print(f"Tuition median: $ {tuition_median:,.0f}")