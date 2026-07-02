# Print All Elements of an Array

arr=[34,67,34,12,89,23]
for i in arr:
    print(i)
    
    
# Sum of Array Elements
arr=[34,67,34,12,89,23]
total=0
for i in arr:
    total = total+i
print("sum:",total)    

# Largest Element
arr=[34,67,34,12,89,23]
largest=arr[0]
for i in arr:
    if i > largest:
        largest=i
print("Largest element:",largest)


# smallest Element
arr=[34,67,34,12,89,23]
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
        
print("Smallest element:",smallest)


#average of Array Elements
arr=[34,67,34,12,89,23]
total=0

for i in arr:
    total +=i
average=total/len(arr)
print("Average:",average)