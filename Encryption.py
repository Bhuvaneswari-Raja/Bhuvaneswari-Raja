import sys 

text = input('Enter text: ')
shift = int(input('Enter shift: '))
d = input('Encrypt or Decrypt:')

if d == 'Decrypt':
	shift = -shift

product = ""

for i in text :
	x = ord(i)
	x = (x + shift - 97) % 26 +97
	product = product + chr(x)


print(product)
