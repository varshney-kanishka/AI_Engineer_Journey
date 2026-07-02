# student marks management system
students=[]
marks=[]

for i in range(4):
    name=input("Enter student name:")
    mark=int(input("Enter student marks:"))
    students.append(name)
    marks.append(mark)
    
    
total=sum(marks)
average=total/len(marks)
highest=max(marks)
lowest=min(marks)

print("/n---------Student Report-----------")

for i in range(4):
    print("Name:",students[i],"Marks:",marks[i]) 
print("Total Marks:",total)
print("Average Marks:",average)
print("Highest Marks:",highest)
print("Lowest Marks:",lowest)