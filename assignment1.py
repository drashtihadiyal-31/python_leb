#Q-1
print("Hello Python!!")
#Q-2
a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
sum = a + b
print("The sum is:", sum)
#Q-3
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
#Q-4
a = int(input("Enter a year: "))
if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
    print(a, "is a Leap Year")
else:
    print(a, "is not a Leap Year")
#Q-5
principal = 1000
rate = 5       
time = 2       
simple_interest = (principal * rate * time) / 100
print("Principal:", principal)
print("Simple Interest:", simple_interest)
print("Total Amount:", principal + simple_interest)
#Q-6
pi=3.14
print(pi)
#Q-7
num = int(input("Enter a number: "))
print("Square is:", num ** 2)
#Q-8
radius = 5
area = 3.14 * radius * radius
print("Area of circle:", area)
#Q-9
x = 10
print(type(x))      
y = 3.14
print(type(y))      
z = "Hello"
print(type(z))      
#Q-10
from math import sqrt, pi
print(sqrt(25))  
print(pi)
#Q-11
print("power:",2**3)
#Q-12
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")



