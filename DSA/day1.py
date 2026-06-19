# Day 1 DSA Problems

# 1. Count Digits
n = int(input("Enter number: "))
count = 0

temp = n
while temp > 0:
    temp = temp // 10
    count += 1

print("Digits =", count)


# 2. Reverse Number
n = int(input("Enter number: "))
rev = 0

temp = n
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse =", rev)


# 3. Palindrome Check
n = int(input("Enter number: "))
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")