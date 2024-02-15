import sys

x = int(input("Enter number: "))

def factorial(number):
	if number == 0:
		return 1
	elif number > 0:
		return number *factorial(number - 1)

print (factorial(x))