import sqlite3
import pandas as pd

# Path to your database file
db_path = 'C:\\Users\\user\\Desktop\\Bi and Ai\\BI-and-AI\\myenv\\lesson9\\population.db'
conn = sqlite3.connect(db_path)

# Task queries
task1 = """
select first_name as FirstName, last_name AS LastName, salary as Salary, gender as Gender, state as State
from population
where gender = 'Female' and state = 'Florida';
"""
result1 = pd.read_sql(task1, conn)

task2 = """
select gender, count(*) as count
from population
where email like '%@apache.org'
group by gender;
"""
result2 = pd.read_sql(task2, conn)

task3 = """
select count(*) AS Malecount
from population
where gender = 'Male' and salary > 1000000;
"""
result3 = pd.read_sql(task3, conn)

task4 = """
select first_name AS FirstName, last_name AS LastName, salary AS Salary
from population
where gender = 'Female' and state = 'Alabama' and salary < 800000;
"""
result4 = pd.read_sql(task4, conn)

task5 = """
select count(*) AS TexasHotmailcount
from population
where state = 'Texas' and email like '%@hotmail.com';
"""
result5 = pd.read_sql(task5, conn)

task6 = """
select first_name AS FirstName, last_name AS LastName, salary AS Salary
from population
where gender = 'Male' and state = 'California' and salary BETWEEN 400000 and 900000;
"""
result6 = pd.read_sql(task6, conn)

task7 = """
select count(*) AS Femalecount
from population
where gender = 'Female' and state = 'New York' and salary > 500000;
"""
result7 = pd.read_sql(task7, conn)

task8 = """
select first_name AS FirstName, last_name AS LastName, salary AS Salary
from population
where state = 'Georgia'
order by salary DESC
LIMIT 10;
"""
result8 = pd.read_sql(task8, conn)

task9 = """
select count(*) AS count
from population
where last_name like 'S%' and salary > 300000;
"""
result9 = pd.read_sql(task9, conn)

task10 = """
select AVG(salary) AS AverageSalary
from population
where gender = 'Female' and state = 'Oklahoma';
"""
result10 = pd.read_sql(task10, conn)

task11 = """
select first_name AS FirstName, last_name AS LastName, email AS Email
from population
where state = 'Florida' and email like '%.net';
"""
result11 = pd.read_sql(task11, conn)

task12 = """
select count(*) AS count
from population
where first_name like 'K%' and salary > 1000000;
"""
result12 = pd.read_sql(task12, conn)

task13 = """
select first_name AS FirstName, last_name AS LastName, email AS Email, salary AS Salary
from population
where email like '%@gmail.com' and salary < 200000;
"""
result13 = pd.read_sql(task13, conn)

task14 = """
select min(salary) AS minSalary
from population
where gender = 'Male' and state = 'Ohio';
"""
result14 = pd.read_sql(task14, conn)

task15 = """
select count(*) AS count
from population
where gender = 'Female' and state = 'California' and salary > 800000;
"""
result15 = pd.read_sql(task15, conn)

task16 = """
select last_name AS LastName, salary AS Salary
from population
where gender = 'Male' and salary > 1200000;
"""
result16 = pd.read_sql(task16, conn)

task17 = """
select first_name AS FirstName, last_name AS LastName, email AS Email, salary AS Salary
from population
where email like '%edu%' and salary > 1500000;
"""
result17 = pd.read_sql(task17, conn)

task18 = """
select count(*) AS count
from population
where state = 'Alabama' and salary < 100000;
"""
result18 = pd.read_sql(task18, conn)

task19 = """
select last_name AS LastName, salary AS Salary
from population
where last_name like '%n' and salary > 600000;
"""
result19 = pd.read_sql(task19, conn)

task20 = """
select max(salary) AS maxSalary
from population
where state = 'District of Columbia';
"""
result20 = pd.read_sql(task20, conn)

task21 = """
select first_name AS FirstName, last_name AS LastName, salary AS Salary
from population
where gender = 'Female' and state = 'New York' and salary BETWEEN 500000 and 1000000;
"""
result21 = pd.read_sql(task21, conn)

task22 = """
select count(*) AS count
from population
where state = 'Texas' and email like '%@yahoo.com';
"""
result22 = pd.read_sql(task22, conn)

task23 = """
select first_name AS FirstName, last_name AS LastName, salary AS Salary
from population
where salary < (
    select AVG(salary)
    from population
    where gender = 'Male' and state = 'California'
);
"""
result23 = pd.read_sql(task23, conn)

# Display results
print("Task 1: Females from Florida")
print(result1)

print("\nTask 2: Males and Females with emails ending in @apache.org")
print(result2)

print("\nTask 3: count of males earning more than 1M")
print(result3)

print("\nTask 4: Females from Alabama with salary below 800K")
print(result4)

print("\nTask 5: People from Texas with emails ending in @hotmail.com")
print(result5)

print("\nTask 6: Males earning between 400K and 900K in California")
print(result6)

print("\nTask 7: count of females from New York with salary over 500K")
print(result7)

print("\nTask 8: Top 10 highest-paid people from Georgia")
print(result8)

print("\nTask 9: People with last names starting with S and earning more than 300K")
print(result9)

print("\nTask 10: Average salary of all females in Oklahoma")
print(result10)

print("\nTask 11: People from Florida with emails ending with .net")
print(result11)

print("\nTask 12: count of people with first names starting with K and salary above 1M")
print(result12)

print("\nTask 13: People with gmail.com in their email and a salary below 200K")
print(result13)

print("\nTask 14: minimum salary for males from Ohio")
print(result14)

print("\nTask 15: count of females from California with salary above 800K")
print(result15)

print("\nTask 16: Last names and salaries of males earning over 1.2M")
print(result16)

print("\nTask 17: People with edu in their email and salary above 1.5M")
print(result17)

print("\nTask 18: count of people living in Alabama with salary below 100K")
print(result18)

print("\nTask 19: People with last names ending in n and salaries above 600K")
print(result19)

print("\nTask 20: Highest salary in District of Columbia")
print(result20)

print("\nTask 21: Females from New York with salaries between 500K and 1M")
print(result21)

print("\nTask 22: People from Texas who have yahoo.com in their email")
print(result22)

print("\nTask 23: Females with salary below the average for males in California")
print(result23)

# Close the database connection
conn.close()
