#Arithmetic operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#salary calculator
salary = float(input("Enter your basic salary: "))
da = 20 * salary / 100
hra = 15 * salary / 100
print("Your salary with 20% DA is:",salary + da)
print("Your salary with 15% HA is:",salary + da + hra)
print("Your total salary is:",salary + da + hra)

#student marks calculator
name = input("Enter student name: ")
m1 = int(input("Enter python marks: "))
m2 = int(input("Enter java marks: "))
m3 = int(input("Enter SQL marks: "))
total = m1 + m2 + m3
average = total / 3
print("\n----Student Marks Report----")
print("Student Name:", name)
print("Python Marks:", m1)
print("Java Marks:", m2)
print("SQL Marks:", m3)
print("Total Marks:", total)
print("Average Marks:", average)

#shopping bill calculator
price1 = float(input("Enter product 1 price: "))
price2 = float(input("Enter product 2 price: "))
price3 = float(input("Enter product 3 price: "))
total = price1 + price2 + price3
discount = total * 0.10
final_amount = total - discount
print("Discount:", discount)
print("Final Amount:", final_amount)

#assignment operators
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

#bank balance
balance = 10000
deposit = 5000
balance += deposit
print("After deposit balance:", balance)
withdraw = 2000
balance -= withdraw
print("After withdrawal balance:", balance)

#comparison operators
a = 10
b = 20
print (a==b)
print (a!=b)
print (a>b)
print (a<b)
print (a>=b)
print (a<=b)

#age eligibility checker
age = int(input("Enter your age: "))
print("Eligigble to vote:", age >= 18)

#pass or fail checker
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")

#login validation
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid credentials")