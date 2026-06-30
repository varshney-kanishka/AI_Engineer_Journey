# print 1 to n
n=int(input("Enter number: "))
for i in range(1,n+1):
    print(i)
    
    
    
#Even Numbers
n=int(input("Enter number: "))
for i in range(2,n+1,2):
  
    print(i)    
    
#factorial
n=int(input("Enter number: "))
fact=1

for i in range(1,n+1):
    fact=fact*i
    
print("Factorial of",n,"is",fact)    


#Prime Number
n=int(input("Enter number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1    
        
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    
    
#fibonacci Series
n=int(input("Enter number: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c   