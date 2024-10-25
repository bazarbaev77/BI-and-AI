#1
# a = float(input('Please enter the value: '))
# p = 4 * a
# print(f'The perimeter of the square is: {p}')

#2
# a = float(input('Iltimos kvadratning tomonini kiriting: '))
# S = a ** 2  # a^2
# print(f'Kvadratning yuzasi : {S}ga teng')

#3
# a = float(input('Iltimos kvadratning a tomonini kiriting: '))
# b = float(input('Iltimos kvadratning b tomonini kiriting: '))
# s = a * b 
# p = 2 * (a + b)
# print(f'Kvadratning yuzasi {s}ga teng')
# print(f'Perimetr {p}ga teng')

#4
# d = float(input('Iltimos diametrni kiriting: '))
# l = 3.14 * d
# print(f'Aylananing yuzi {l}ga teng')

#5
# a = float(input('Kubning yon tomon qiymatini kiriting: '))
# v = a**3
# s = 6*a**2
# print(f'Kubning hajmi teng {v} tola sirti teng {s}')

#6
# a = float(input('tomonlar qiymatini kiriting a: '))
# b = float(input('tomonlar qiymatini kiriting b: '))
# c = float(input('tomonlar qiymatini kiriting c: '))

# v = a*b*c 
# s = 2*(a*b+b*c+a*c)
# print(f'Javoblar v teng {v}, s teng {s}')

#7
# R = float(input('Enter the R: ')) 
# l = 2 * 3.14 * R
# s = 3.14 * (R**2)
# print(f'Answers: L = {l}, S = {s}')

#8
# a = float(input('Enter the a: '))
# b = float(input('Enter the b: '))

# t = (a+b)/2
# print(f'Answer is {t}')

#9
# import math 
# a = float(input('Enter the a: '))
# b = float(input('Enter the b: '))

# geometric_mean = math.sqrt(a * b)

# print(f'Answer is {geometric_mean}')

#10
# a = float(input('Enter the a: '))
# b = float(input('Enter the b: '))
# while a == 0 or b == 0:
#     print(f"a or b should not be equal to 0.")
#     a = float(input('Enter the a: '))
#     b = float(input('Enter the b: '))
# yigindi = a + b
# kopaytma = a * b
# ayirma = a / b
# print(f'yigindi: {yigindi}\n'
#       f'kopaytma: {kopaytma}\n'
#       f'ayirma: {ayirma}')

#11
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# yigindi = a + b
# kopaytma = a * b
# mod_a = abs(a)
# mod_b = abs(b)
# print(f"Yig'indi: {yigindi}")
# print(f"Ko'paytma: {kopaytma}")
# print(f"Birinchi sonning moduli: {mod_a}")
# print(f"Ikkinchi sonning moduli: {mod_b}")

#12
# import math

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))

# h = math.sqrt(a**2 + b**2)
# p = a + b + h
# print(f"Hypotenuse: {h:.2f}")
# print(f"Perimeter: {p:.2f}")


#14
# L = float(input("Aylaning uzunligini kiriting (L): "))
# pi = 3.14
# R = L / (2 * pi)
# S = pi * R ** 2
# print(f"Aylaning radiusi: {R}, Yuzi: {S}")

#15
# S = float(input("Aylaning yuzasini kiriting (S): "))
# pi = 3.14
# R = (S / pi) ** 0.5
# d = 2 * R
# print(f"Aylaning radiusi: {R}, Diametri: {d}")

#16
# z1 = float(input("Birinchi nuqta (z1) ni kiriting: "))
# z2 = float(input("Ikkinchi nuqta (z2) ni kiriting: "))
# distance = (z2 - z1)
# print(f"Ikki nuqta orasidagi masofa: {distance}")

#17
# A = float(input("A nuqtani kiriting: "))
# B = float(input("B nuqtani kiriting: "))
# C = float(input("C nuqtani kiriting: "))

# AC = (C - A)
# BC = (C - B)

# print(f"AC kesmaning uzunligi: {AC}")
# print(f"BC kesmaning uzunligi: {BC}")


#18
# x1 = float(input("Birinchi nuqtaning x1 koordinatasini kiriting: "))
# y1 = float(input("Birinchi nuqtaning y1 koordinatasini kiriting: "))
# x2 = float(input("Ikkinchi nuqtaning x2 koordinatasini kiriting: "))
# y2 = float(input("Ikkinchi nuqtaning y2 koordinatasini kiriting: "))

# d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print(f"Ikki nuqta orasidagi masofa: {d}")


#19
# l = float(input("To'rtburchakning uzunligini kiriting: "))
# w = float(input("To'rtburchakning kengligini kiriting: "))

# p = 2 * (l + w)
# a = l * w

# print(f"To'rtburchakning perimetri: {p}")
# print(f"To'rtburchakning yuzi: {a}")

# #20
# x1 = float(input("Birinchi nuqtaning x1 koordinatasini kiriting: "))
# y1 = float(input("Birinchi nuqtaning y1 koordinatasini kiriting: "))
# x2 = float(input("Ikkinchi nuqtaning x2 koordinatasini kiriting: "))
# y2 = float(input("Ikkinchi nuqtaning y2 koordinatasini kiriting: "))

# d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print(f"Tekislikdagi ikkita nuqta orasidagi masofa: {d}")

#21
# r = float(input("Aylananing radiusini kiriting: "))

# c = 2 * 3.14159 * r
# a = 3.14159 * r**2

# print(f"Aylananing uzunligi: {c}")
# print(f"Aylananing yuzi: {a}")

#22
# s = float(input("Kubning tomonini kiriting: "))

# v = s**3
# s = 6 * s**2

# print(f"Kubning hajmi: {v}")
# print(f"Kubning sirti: {s}")

#23
# l = float(input("Uzunlikni kiriting: "))
# w= float(input("Kenglikni kiriting: "))
# h = float(input("Balandlikni kiriting: "))

# v = l * w * h
# s = 2 * (l * w + w * h + h * l)

# print(f"Turtburchakli parallelepipedning hajmi: {v}")
# print(f"Turtburchakli parallelepipedning sirti: {s}")

# #24
# r = float(input("Tsilindrning radiusini kiriting: "))
# h = float(input("Tsilindrning balandligini kiriting: "))

# v = 3.14159 * r**2 * h
# s = 2 * 3.14159 * r * (r + h)

# print(f"Tsilindrning hajmi: {v}")
# print(f"Tsilindrning sirti: {s}")

#25
# d = float(input("Burchakni darajalarda kiriting: "))

# r = d * 3.14159 / 180
# print(f"burchak radianlarda: {r}")

# #26
# radians = float(input("Burchakni radianlarda kiriting: "))

# degrees = radians * 180 / 3.14159
# print(f"burchak darajalarda: {degrees}")

# #27
# fahrenheit = float(input("fahrenheitda haroratni kiriting: "))

# celsius = (fahrenheit - 32) * 5 / 9
# print(f"Harorat Selsiyda: {celsius}")

# #28
# celsius = float(input("selsiyda haroratni kiriting: "))

# fahrenheit = (celsius * 9 / 5) + 32
# print(f"harorat Fahrenheitda: {fahrenheit}")

# #29
# kilometers = float(input("Kilometrlarni kiriting: "))

# miles = kilometers * 0.621371
# print(f"Mil: {miles}")

# #30
# miles = float(input("millarni kiriting: "))

# kilometers = miles / 0.621371
# print(f"Kilometr: {kilometers}")

# #31
# F = float(input("farengeyt qiymatini kiriting: "))
# C = (F - 32) * 5 / 9
# print(f"selsiy bo'yicha temperatura: {C}")

# #32
# C = float(input("selsiy qiymatini kiriting: "))
# F = (C * 9 / 5) + 32
# print(f"Farengeyt bo'yicha temperatura: {F}")

# #33
# x = float(input("A ning narxi (so'm/kg) ni kiriting: "))
# y = float(input("b ning narxi (so'm/kg) ni kiriting: "))
# cost_x = x * 1 
# cost_y = y * 1 
# print(f"1 kg A ning narxi {cost_x}, 1 kg B ning narxi {cost_y}")

# #34
# x_chocolate = float(input("shokolad narxi (so'm/kg) ni kiriting: "))
# y_candy = float(input("Konfet narxi (so'm/kg) ni kiriting: "))
# kg_chocolate = float(input("necha kg shokolad: "))
# kg_candy = float(input("necha kg konfet: "))
# total_cost = (x_chocolate * kg_chocolate) + (y_candy * kg_candy)
# print(f"umumiy narxi {total_cost} so'm bo'ladi.")

# #35
# v_boat = float(input("Qayiqning tezligi (km/soat): "))
# u_river = float(input("Daryo oqimi tezligi (km/soat): "))
# time_against_flow = float(input("Qayiqning oqimga qarshi harakatlanish vaqti (soat): "))
# distance = time_against_flow * (v_boat - u_river)
# print(f"Yurilgan masofa: {distance} km")

# #36
# v1 = float(input("Birinchi avtomobilning tezligi (km/soat): "))
# v2 = float(input("Ikkinchi avtomobilning tezligi (km/soat): "))
# distance_between = float(input("Boshlang'ich masofa (km): "))
# time = float(input("Harakatlanish vaqti (soat): "))
# remaining_distance = distance_between - (v1 + v2) * time
# print(f"Qolgan masofa: {remaining_distance} km")

# #37
# v1 = float(input("Birinchi avtomobilning tezligi (km/soat): "))
# v2 = float(input("Ikkinchi avtomobilning tezligi (km/soat): "))
# distance_between = float(input("Boshlang'ich masofa (km): "))
# time = float(input("Harakatlanish vaqti (soat): "))
# total_distance = distance_between + (v1 + v2) * time
# print(f"Ular orasidagi umumiy masofa: {total_distance} km")

# #38
# A = float(input("A ni kiriting: "))
# B = float(input("B ni kiriting: "))
# C = float(input("C ni kiriting: "))
# if A != 0:
#     x = -C / A
#     print(f"Tenglama yechimi: x = {x}")
# else:
#     print("A 0 ga teng bo'lmasligi kerak.")

# #39
# A = float(input("A ni kiriting: "))
# B = float(input("B ni kiriting: "))
# C = float(input("C ni kiriting: "))
# D = B**2 - 4*A*C  # Discriminant
# if D >= 0:
#     x1 = (-B + D**0.5) / (2*A)
#     x2 = (-B - D**0.5) / (2*A)
#     print(f"Yechimlar: x1 = {x1}, x2 = {x2}")
# else:
#     print("Tenglama haqiqiy ildizga ega emas.")

# #40
# A1 = float(input("A1 ni kiriting: "))
# B1 = float(input("B1 ni kiriting: "))
# C1 = float(input("C1 ni kiriting: "))
# A2 = float(input("A2 ni kiriting: "))
# B2 = float(input("B2 ni kiriting: "))
# C2 = float(input("C2 ni kiriting: "))
# D = A1*B2 - A2*B1
# if D != 0:
#     x = (C1*B2 - C2*B1) / D
#     y = (A1*C2 - A2*C1) / D
#     print(f"Tizim yechimi: x = {x}, y = {y}")
# else:
#     print("Tizimda yechim yo'q.")
