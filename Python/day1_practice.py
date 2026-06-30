# question 1 Take name and print:
name=input("Enter your name: ")
print(name)

#question 2 Take age and print:
age=(input("Enter your age: "))
print("You are",age,"years old.")

#question 3 Take two numbers and print their multiplication:
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))    
print("Product =", num1 * num2)

#question 4 find square of a number:
num=int(input("Enter a number: "))
print("Square =", num **2)

#question 5 find area of circle:
radius=int(input("Enter radius of circle: "))
area=3.14*radius**2
print("Area of circle is: ",area)

#question 6 celcius to farenheit:
celsius=int(input("enter temperature in celsius: "))
farenheit=(celsius*9/5)+32
print("Temperature in farenheit is: ",farenheit)

#question 7 swap two numbers:
a=int(input("Enter first number: "))    
b=int(input("Enter second number: "))
a,b=b,a
print("After swapping: a =",a,"b =",b)

#question 8 find percentage of three subjects:
maths=34
science=56
hindi=67
total=maths+science+hindi
print("total percentage=",(total/300)*100,"%")

#question 9 Mini student card
name = input("Name: ")
age = input("Age: ")
college = input("College: ")
print("-----Student Card-----")
print("Name:", name)
print("Age:", age)
print("College:", college)