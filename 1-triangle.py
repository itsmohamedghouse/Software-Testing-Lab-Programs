# Program Number 7 in Manual

# Design and develop a program in a language of your choice to solve the triangle problem
# defined as follows: Accept three integers which are supposed to be the three sides of a
# triangle and determine if the three values represent an equilateral triangle, isosceles triangle,
# scalene triangle, or they do not form a triangle at all. Derive test cases for your program
# based on decision-table approach, execute the test cases and discuss the results.


a = int(input("Enter first side of triangle:"))
b = int(input("Enter second sides of triangle:"))
c = int(input("Enter third sides of triangle:"))

# Check if triangle is valid
if ((a + b > c) and (a + c > b) and (b + c > a)) :
	print("Triangle is valid.")
	# if valid check the type of triangle
	if a == b == c:
		print("Equilateral triangle")
	elif (a==b or b==c or c==a):
		print("isosceles triangle")
	else:
		print("Scalene triangle")
else :
	print("Triangle is not valid.")