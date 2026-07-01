'''
#####
#####
#####
#####
#####
'''

for i in range(1,6):
    for j in range(1,6):
        print("#",end="")
    print()
    
    
    
'''
*
**
***
****
*****
'''
    
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end="")
    print()   
    
    
        
    
    '''
    ****
    ***
    **
    *
    '''
    
r=4
for i in range(r,0,-1):
    for j in range(i):
        print("*",end="")
    print()       


'''
1
12
123
1234
12345
'''


n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
    
    
    
'''
4321
321
21
1
'''    
n=4
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
    
    n = 5
    
    
'''
    *
   ***
  *****
 *******
*********     
    '''
    

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()