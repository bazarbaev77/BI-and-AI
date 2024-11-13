#1
l = ["apple", "cherry", "apple"]
k = l.count("apple")
print(k)

#2
l = ["apple", "cherry", "apple"]
d = len(l)
print(d)

#3
l = ["apple", "cherry", "apple"]
f = max(l)
print(f)

#4
l = ["apple", "cherry", "apple"]
f = min(l)
print(f)

#5
l = ["apple", "cherry", "apple"]
g = 'banana' in l
print(g)

#6
l = ["apple", "cherry", "apple"]
if l:
    f = l[0]
else:
    f = None  
print(f)  

#7
l = []
if l:
    f = l[-1]
else:
    f = None  
print(f)  

#8
l = ["apple", "cherry", "apple", "banana", "pineapple"]
g = l[:3]
print(g)

#9
l = ["apple", "cherry", "apple", "banana", "pineapple"]
f = l[::-1]
print(f)

#10
l = ["apple", "cherry", "apple", "banana", "pineapple"]
l.sort()
print(l)

#11
l = ["apple", "cherry", "apple", "banana", "pineapple"]
k = set(l)
print(k)

#12
l = ["apple", "cherry", "apple", "banana", "pineapple"]
l.insert(3, "yummy")
print(l) 


#13
l = ["apple", "cherry", "banana", "pineapple"]
k = l.index("banana", 0)
print(k)   

#14
m = ["apple"]
k = len(m) == 0
print(k)

#15
num = [1, 2, 3, 4, 5, 6]
even = 0
for num in num:
    if num % 2 == 0:
        even+= 1
print(even) 

#16
num = [1, 2, 3, 4, 5, 6]
odd = 0
for num in num:
    if num %2 != 0:
        odd+= 1
print(odd) 

#17
a = ['a', 'bn', 'fg', 'ff']
b = a + ['s', 'ss', 'sss']
print(b)

#18
a = ['a', 'bn', 'fg', 'ff']
b = ['s', 'ss', 'fg']

c = any(item in a for item in b)
print(c) 

#19


#20
list = [5, 1, 3, 4, 2, 6]
unique = sorted(set(list), reverse=True)
second = unique[1] if len(unique) > 1 else None
print(second)

#21
list = [5, 1, 3, 4, 2, 6]
unique = sorted(set(list))
second = unique[1] if len(unique) > 1 else None
print(second)

#22
num = [1, 2, 3, 4, 5, 6]
even = [n for n in num if n % 2 == 0]
print(even)

#23
num = [1, 2, 3, 4, 5, 6]
even = [n for n in num if n % 2 != 0]
print(odd)

#25
i = ['l', 'i', 'pp', 'k']
k = i.copy()
print(k)

#24
i = ['l', 'i', 'pp', 'k']
k = len(i)
print(k)

#26
l = [1, 2, 3, 4, 5, 6] 
length = len(l)
if length % 2 == 1:
    middle_index = length // 2
    middle_element = l[middle_index]
    print("Middle element:", middle_element) 
else: 
    middle_index1 = (length // 2) - 1
    middle_index2 = middle_index1 + 1
    middle_elements = l[middle_index1:middle_index2 + 1]
    print("Middle elements:", middle_elements)  

# 27
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
start_index = 2
end_index = 6
max_elem = max(my_list[start_index:end_index])
print("Maximum element of the sublist:", max_elem)

# 28
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
start_index = 2
end_index = 6
min_elem = min(my_list[start_index:end_index])
print("minimum element of the sublist:", min_elem)

# 29
my_list = [3, 1, 4, 1, 5, 9]
index_remove = 2
if 0 <= index_remove < len(my_list):
    my_list.pop(index_remove)
print("List after removal:", my_list)

# 30
list = [1, 2, 3, 4, 5]
is_sorted = list == sorted(list)
print("Is the list sorted?", is_sorted)

# 31
my_list = [1, 2, 3]
repeat_count = 3
repeated_list = [item for item in my_list for i in range(repeat_count)]
print("repeated elements:", repeated_list)

# 32
list1 = [3, 1, 4]
list2 = [1, 5, 9]
merged_sorted = sorted(list1 + list2)
print("merged and sorted list:", merged_sorted)

# 33
my_list = [1, 2, 3, 1, 4, 1]
elem = 1
indices = [i for i, x in enumerate(my_list) if x == elem]
print("Indices: ", indices)

# 34
list = [1, 2, 3, 4, 5]
rotated = [my_list[-1]] + list[:-1]
print("Rotated list:", rotated)

# 35
range_list = list(range(1, 11))
print("Range list:", range_list)

# 36
num_list = [-1, 2, -3, 4, 5]
sum_positive = sum(x for x in num_list if x > 0)
print("Sum of positive numbers:", sum_positive)

# 37
sum_negative = sum(x for x in num_list if x < 0)
print("Sum of negative numbers:", sum_negative)

# 38
my_list = [1, 2, 3, 2, 1]
is_palindrome = my_list == my_list[::-1]
print("Is the list a palindrome?", is_palindrome)

# 39
my_list = [1, 2, 3, 4, 5]
elements_per_sublist = 2
nested_list = [my_list[i:i + elements_per_sublist] for i in range(0, len(my_list), elements_per_sublist)]
print("Nested list:", nested_list)

# 40
my_list = [1, 2, 1, 3, 2, 4]
unique_list = []
for x in my_list:
    if x not in unique_list:
        unique_list.append(x)
print("elements in order:", unique_list)


#Tuples
#1
t = (1, 2, 3, 1, 4, 1, 5)
elem = 1
count = t.count(elem)
print("element appears", count, "times")

#2
t = (1, 2, 3, 1, 4, 1, 5)
r = max(t)
print(t)

#3
t = (1, 2, 3, 1, 4, 1, 5)
r = min(t)
print(t)

#4
t = (1, 2, 3, 1, 4, 1, 5)
r = r in t 
print(r)

#5
t = (10, 20, 30)

first_elem = t[0] if t else None
print("The first element is:", first_elem)

#6
t = (10, 20, 30)

first_elem = t[-1] if t else None
print("The first element is:", first_elem)

#7
t = (10, 20, 30)

first_elem = len(t)
print("The first element is:", first_elem)

#8
t = (10, 20, 30)
first_three = t[:3]
print(first_three)

#9
t = (10, 20, 30)
f = (10, 20, 30)
d = t+ f
print(d)

#10
t = ()

if len(t) > 0:
    print("The tuple has elements.")
else:
    print("The tuple is empty.")

#11
my_tuple = (10, 20, 30, 20, 40, 20)
element = 20

indices = [index for index, value in enumerate(my_tuple) if value == element]
print("number  of the element in the tuple:", indices)

#13
tuple = (10, 20, 30, 40, 20)
sort = sorted(set(my_tuple))
high_val = sort[1]
print("The second largest element is:", high_val)

#12
my_tuple = (10, 20, 30, 40, 20)
unique_sorted = sorted(set(my_tuple))
second_smallest = unique_sorted[1]
print("The second smallest element is:", second_smallest)

#14
element = 42
single_element_tuple = (element,)
print("Tuple with a single element:", single_element_tuple)

#15
t = [1, 2, 3, 4, 5, 6]
e = tuple(t)
print(e)

#16
start, end = 1, 5
max_of_subtuple = max(t)
print(max_of_subtuple)  

#17
min_of_subtuple = min(t)
print(min_of_subtuple)

#18
value_to_remove = 1
t_list = list(t)
if value_to_remove in t_list:
    t_list.remove(value_to_remove)
new_tuple = tuple(t_list)
print(new_tuple) 

#19
n = 3
nested_tuple = tuple(t[i:i + n] for i in range(0, len(t), n))
print(nested_tuple) 

#20
repeat_count = 2
repeated_tuple = tuple(element for element in t for _ in range(repeat_count))
print(repeated_tuple) 

#21
start_range, end_range = 1, 10
range_tuple = tuple(range(start_range, end_range + 1))
print(range_tuple)

#22
reversed_tuple = t[::-1]
print(reversed_tuple) 

#23
is_palindrome = t == t[::-1]
print(is_palindrome)

#24
seen = set()
unique_elements = []
for element in t:
    if element not in seen:
        seen.add(element)
        unique_elements.append(element)
unique_tuple = tuple(unique_elements)
print(unique_tuple) 

#SEt

#1
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 / set2
print(set3)

#2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1 - set2
print(set3)


#3
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common_set = set1.intersection(set2)
print(common_set)

#4
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1 < set2
print(is_subset)

#5
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = set2 in set1 
print(set3)

#6
set = {1, 2, 3, 4, 5, 5, 6}
r = len(set)
print(r)

#7
l = [1, 2, 2, 3, 4, 4, 5]
u = set(l)
print(u)

#8
set = {1, 2, 3, 4, 5}
e = 3
set.remove(e)
print(set)

#9
set = {1, 2, 3, 4, 5}
set2 = set.clear()
print(set2)

#10
l = [1, 2, 3]  
if len(l) > 0:
    print("The list has elements.")
else:
    print("The list is empty.")

#11
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
diff = set_a ^ set_b 
print("elements:", diff)

#12
set = {1, 2, 3}
elem = 4
set.add(elem)
print(set)

#13
set = {1, 2, 3, 4, 5}
elem = set.pop()
print("Removed element:", elem)
print("Updated set:", set)

#14
set = {3, 7, 2, 9, 5}
max_elem = max(set)
print("Max elem:", max_elem)

#15
set = {3, 7, 2, 9, 5}
max_elem = max(set)
print("Min elem:", max_elem)

#16
numbers = {1, 2, 3, 4, 5, 6}
even_numbers = {num for num in numbers if num % 2 == 0}

#17
numbers = {1, 2, 3, 4, 5, 6}
odd_numbers = {num for num in numbers if num % 2 != 0}

#18
range = set(range(1, 11))

#19
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged_set = set(list1) | set(list2)

#20
set1 = {1, 2, 3}
set2 = {4, 5, 6}
disjoint = set1.isdisjoint(set2)

#21
list = [1, 2, 2, 3, 4, 4]
unique = list(set(my_list))

#22
list = [1, 2, 2, 3, 4, 4]
unique = list(dict.fromkeys(my_list))

#23
sets = {frozenset({i, i + 1}) for i in range(1, 5)}

#24
list = [1, 2, 2, 3, 4, 4]
unique = len(set(my_list))

#25
import random
random_set = {random.randint(1, 100) for i in range(10)}

#Dictionary

dict = {'a': 1, 'b': 2}
value = dict.get('c', 'default_value')

#2
dict = {'a': 1, 'b': 2}
key = 'a' in dict
print(key)

#3
key_count = len(dict)

#4
keys = list(dict.keys())

#5
values = list(dict.values())
print(values)

#6
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
mdict = {**dict1, **dict2}
print(mdict)

#7
print(dict.pop('a', None))

#8
dict = {}
dict.clear()

#9
dict1 = {'a': 1, 'b': 2}
is_empty = not dict1
print(is_empty)

#10
my_dict = {'a': 1, 'b': 2}
pair = (key, my_dict[key]) if key in my_dict else None

#11
new_value = {}
my_dict[key] = new_value

#12
count = list(my_dict.values()).count(value)

#13
inverted_dict = {v: k for k, v in my_dict.items()}

#15
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))

#16
has_nested = any(isinstance(v, dict) for v in my_dict.values())

#19
unique_value_count = len(set(my_dict.values()))

#20
sorted_by_key = dict(sorted(my_dict.items()))

#23
common_keys = set(dict1.keys()) & set(dict2.keys())

#24
my_tuple = (('a', 1), ('b', 2))
my_dict = dict(my_tuple)
print(my_dict)

#25
first_pair = next(iter(my_dict.items())) if my_dict else None
print(first_pair)