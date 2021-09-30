x = float(input("Enter a number between 1 and 10: "))

if x >= 1 and x <= 10:
	print("The number you entered is ",x)
elif x <= 1:
	print("The number you entered is < 1")
elif x >= 10:
	print("The number you entered is > 10")
else:
	print("Invalid input")
