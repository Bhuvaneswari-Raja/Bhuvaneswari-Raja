
while True:
	num1 = input("First Number: ")
	operator = input("Operator (+, -, *, /): ")
	num2 = input("Second Number: ")

	num1 = float(num1)
	num2 = float(num2)

	out = None
	if operator == "+":
	    out =  num1 + num2
	elif operator == "-":
	    out = num1 - num2
	elif operator == "*":
	    out = num1 * num2
	elif operator == "/":
	    out = num1 / num2
	    
	print("Answer: " + str(out))

	String_1 = input("Do you want to contiue? ")

	if String_1 == "no":
		break
