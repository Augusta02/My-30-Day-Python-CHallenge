# Day 3 of 30Day of Python
age= 25
height = 165
com_var= 4 + 5j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# base = input("Enter base: ")
# height = input('Enter height: ')
# area_of_triangle = 0.5 * base * height
# print('The area of the triangle: ', area_of_triangle)

# # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# a = input('Enter side a: ')
# b = input('Enter side b: ')
# c = input('Enter side c: ')
# perimeter = a + b + c
# print('The perimeter of the triangle: ', perimeter)

# # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# length = input('Enter lenght:')
# width = input('Enter width: ')
# area = length * width
# print(area)

# perimeter = 2 * (length + width)
# print(perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# radius = input('Enter a number: ')
# pi = 3.14
# area = pi * radius ** 2
# circumference = 2 * pi * radius

# print('The area of the circle:', area)
# print('The circumference of a circle:', circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2


# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2 = 2, 3
y1, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
print(m)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0. 

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pyt_len = len('python')
dra_len = len('dragon')
print(pyt_len > dra_len)


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and  'on'in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

# Find the length of the text python and convert the value to float and convert it to string
pyth= len('python')
print(pyth)
pyth_ = float(pyth)
print(pyth_)
str_pyth= str(pyth_)
print(str_pyth)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = 5
y = x % 2 == 0
print(y)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
y = 7 // 3
x = y == 2.7
print(x)

# Check if type of '10' is equal to type of 10
print('10' == 10)

# Check if int('9.8) equal 10
print(int(9.8) == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours: ')
rate_per_hour = input("Enter rate per hour: ")
weekly_earning = hours * rate_per_hour
print(weekly_earning)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years= input('Enter number of years you have lived: ')
num_of_secs_per_year = 365 * 86400
print(number_of_years * num_of_secs_per_year)