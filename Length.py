import sys 

name = (input("Enter text: "))

def length(n):
	counter = 0
	for c in n: 
	    counter+=1 
	return counter

print(length(name))
