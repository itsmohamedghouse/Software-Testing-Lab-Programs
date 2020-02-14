print("Enter three sides of triangle: \n")
a = int(input())
b = int(input())
c = int(input())
if a > 10 or b >10 or c > 10:
	print("Enter values less than 10")
elif ((a + b > c) and (a + c > b) and (b + c > a)) :
	print("Triangle is valid.")
	if a == b == c:
		print("Equilateral triangle")
	elif a==b or b==c or c==a:
		print("isosceles triangle")
	else:
		print("Scalene triangle")
else :
	print("Triangle is not valid.")