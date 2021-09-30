x = int(input("Enter score: "))

if x >= 90 and x <= 100:
	score = "A"
elif x >= 80 and x <= 89:
	score = "B"
elif x >= 70 and x <= 79:
	score = "C"
elif x >= 60 and x <= 69:
	score = "D"
elif x < 60:
	score = "F"
else:
	print("Invalid input")

print("The letter grade is",score)
