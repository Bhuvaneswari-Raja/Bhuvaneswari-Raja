import sys

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sum = 0

for x in range (a,b +1):
	sum = x + sum

print(sum)