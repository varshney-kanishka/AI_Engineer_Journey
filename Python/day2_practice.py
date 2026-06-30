 #Even/Odd no.
n=int(input("enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")    
    
  # positive. negative or zero  

a=int(input("enter a number:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")        
    
    
# greater of two numbers    
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>b:
    print(a,"is greater")
else:
    print(b,"is greater")    
    
    
#leap year or not
year=int(input("enter a year:"))
if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")        
    
 
 
#print("numbers from 1 to 100")
for i in range(1,101):
    print(i)
    
    
#sum of first n numbers    
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of first",n,"numbers is",sum)    

# multiplication table of a number
n=int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    


#factorial of a number
n=int(input("enter a number:"))
total=1
for i in range(1,n+1):
    total=total*i
print("factorial of",n,"is",total)    