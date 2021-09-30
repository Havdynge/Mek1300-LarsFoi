from math import pi
x = input("Enter 'c' for circle or 's' for sphere")
r = int(input("Enter a radius: "))

if x == "c": 
	print(f"Area of the circle: { pi * r ** 2:.2f}")
	print(f"Circumference of the circle: { 2 * pi * r:.2f}")
elif x == "s":
	print(f"Volume of the sphere: {(4 / 3) * pi * r**3:.2f}")
	print(f"surface area of the sphere: {4 * pi *r**2:.2f}")
else:
	print("Please enter a valid option")
