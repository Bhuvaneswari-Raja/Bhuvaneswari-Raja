
w = int(input("Enter weight: "))
h = int(input("Enter height: "))


def calculator(height, weight):
	bmi = 703*(weight/height)**2
	return bmi

my_bmi = calculator(w,h)
print(my_bmi)