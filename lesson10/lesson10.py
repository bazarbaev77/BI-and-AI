import pandas as pd
import matplotlib.pyplot as plt

#1
# data2 = {
#     'date': pd.date_range(start='2023-01-01', periods=10),
#     'productA': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
#     'productB': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
#     'productC': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
# }

# df2 = pd.DataFrame(data2)

# total_sales = df2[['productA', 'productB', 'productC']].sum()
# print("total sales for each product:")
# print(total_sales)

# df2['total sales'] = df2[['productA', 'productB', 'productC']].sum(axis=1)
# date_highest_sales = df2.loc[df2['total sales'].idxmax(), 'date']
# print("date with the highest total sales:", date_highest_sales)

# percentage_change = df2[['productA', 'productB', 'productC']].pct_change() * 100
# print("percentage change in sales for each product:")
# print(percentage_change)

# plt.figure(figsize=(10, 6))
# plt.plot(df2['date'], df2['productA'], label='productA', marker='o')
# plt.plot(df2['date'], df2['productB'], label='productB', marker='o')
# plt.plot(df2['date'], df2['productC'], label='productC', marker='o')
# plt.xlabel('date')
# plt.ylabel('sales')
# plt.title('sales trends for each product over time')
# plt.legend()
# plt.grid()
# plt.show()


# #2
# data3 = {
#     'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
#     'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
#     'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
#     'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
# }

# df3 = pd.DataFrame(data3)

# max_experience_employee = df3.loc[df3['Experience (Years)'].idxmax(), 'Name']
# print("Employee with the highest experience:", max_experience_employee)

# avg_salary = df3['Salary'].mean()
# print("\nAverage salary for all employees:", avg_salary)

# df3['SalaryPctChange'] = df3['Salary'].pct_change() * 100
# print("\nPercentage change in salary for each employee:")
# print(df3[['Name', 'SalaryPctChange']])

# department_counts = df3['Department'].value_counts()

# plt.figure(figsize=(10, 6))
# department_counts.plot(kind='bar', color='skyblue')
# plt.title('Distribution of Employees Across Departments')
# plt.xlabel('Department')
# plt.ylabel('Number of Employees')
# plt.xticks(rotation=45) 
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()


#3
# data4 = {
#     'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
#     'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
#     'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
#     'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
# }

# df4 = pd.DataFrame(data4)

# total_revenue = df4['Total_Price'].sum()
# print("total revenue from all orders:", total_revenue)

# most_ordered_product = df4['Product'].mode()[0]
# print("\nmost ordered product:", most_ordered_product)

# average_quantity = df4['Quantity'].mean()
# print("\naverage quantity of products ordered:", average_quantity)

# sales_distribution = df4.groupby('Product')['Total_Price'].sum()
# plt.figure(figsize=(8, 8))
# sales_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
# plt.title('sales distribution across products')
# plt.ylabel('') 
# plt.show()
