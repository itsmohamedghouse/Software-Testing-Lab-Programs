# Program Number 1 and 4 in Manual

# Design and develop a program in a language of your choice to solve the triangle problem
# defined as follows: Accept three integers which are supposed to be the three sides of a
# triangle and determine if the three values represent an equilateral triangle, isosceles triangle,
# scalene triangle, or they do not form a triangle at all. Assume that the upper limit for the
# size of any side is 10. Derive test cases for your program based on boundary-value analysis,
# execute the test cases and discuss the results. 

# Design and develop a program in a language of your choice to solve the triangle problem
# defined as follows: Accept three integers which are supposed to be the three sides of a
# triangle and determine if the three values represent an equilateral triangle, isosceles triangle,
# scalene triangle, or they do not form a triangle at all. Assume that the upper limit for the
# size of any side is 10. Derive test cases for your program based on equivalence class
# partitioning, execute the test cases and discuss the results.

while True:
	a = int(input("Enter first side of triangle:"))
	b = int(input("Enter second sides of triangle:"))
	c = int(input("Enter third sides of triangle:"))
	if a <= 1 or a >= 10 :
		print(f"The value of a : {a} is not in the range of permitted value")
	if b <= 1 or b >= 10:
		print(f"The value of b : {b} is not in the range of permitted value")
	if c <= 1 or c >= 10:
		print(f"The value of c : {c} is not in the range of permitted value")
	else:
		break

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