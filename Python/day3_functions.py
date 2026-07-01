# average
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    average = (a + b + c) / 3
    print(average)
avg()   
avg()   
avg()   
avg()   


# greet
def greet():
    print("GoodDay")
greet()


#function with arguments
def greet(name,ending):
    print("good day ," + name)
    print (ending)

greet("Kanishka","bye")
greet("Varshney","see you")
greet("Python","bye")    
          
          
def greet(name,ending="sorry"):
    print("good day ," + name)
    print (ending)

greet("Kanishka")
greet("Varshney")
greet("Python","bye") 

# recursion 
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
n=int(input("enter a number:"))
print("factorial of",n,"is",factorial(n))


# greatest of 3 numbers
def greatest(a,b,c): 
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
a=1
b=2
c=3
print(greatest(a,b,c))    
  


# sum of n numbers using recursion
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(10))      
  


#pattern using function
def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)

pattern(7)



#multiplication table using function
def multiply (n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
multiply(10)        