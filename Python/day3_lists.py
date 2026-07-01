# generating list
fruits=["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

# print first element
a=["harry",98,"global",45.9]
print(a[0])

# print last element
a=["harry",98,"global",45.9]
print(a[-1])

# append a new number to the list
a=[45,78,23,12,67]
a.append(23)
print(a)
   
   
# remove a number from the list
a=[45,78,23,12,67]
a.remove(45)
print(a)


#sorting a list
a=[45,78,23,12,67]
a.sort()
print(a)


#insert a number at a specific index
a=[45,78,23,12,67]
a.insert(4,68)
print(a)


#reverse a list
a=[45,78,23,12,67]
a.reverse()
print(a)

# Take 5 numbers from the user
a1=int(input("Enter number 1:"))
a2=int(input("Enter number 2:"))
a3=int(input("Enter number 3:"))
a4=int(input("Enter number 4:"))
a5=int(input("Enter number 5:"))

numbers=[a1,a2,a3,a4,a5]
numbers.sort()
print("Numbers in list:",numbers)




# write a program to accept marks of 6 students and display them in sorted manner
marks=[]
a1=int(input("Enter marks of student 1:"))
marks.append(a1)
a2=int(input("Enter marks of student 2:"))
marks.append(a2)
a3=int(input("Enter marks of student 3:"))
marks.append(a3)
a4=int(input("Enter marks of student 4:"))
marks.append(a4)
a5=int(input("Enter marks of student 5:"))
marks.append(a5)
a6=int(input("Enter marks of student 6:"))
marks.append(a6)
marks.sort()
print("Marks in list:",marks)


#sum of all numbers in a list
numbers=[12,45,67,23,89]
print(sum(numbers))