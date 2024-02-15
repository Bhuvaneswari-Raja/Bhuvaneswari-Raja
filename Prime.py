import sys

x = int(input("Enter a number: "))
y = ''

for i in range(1, x+1):
	y = y + "  " + str(i)
	print(y)