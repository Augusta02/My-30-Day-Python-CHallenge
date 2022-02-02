#"Day 2: 30 Days of Python Programming"
first_name=  'Augusta'
last_name= 'Alokam'
full_name= 'Alokam Chinenyenwa Abosede Augusta'
country = 'Nigeria'
city = 'Lagos'
Age = 25
current_year= 2022
is_married = False
is_true = 'Will be making 300,000 this year'
is_light_on= True
middle_name, age, previous_year= 'Chinenyenwa', 25, 2021

#Exercise: Level 2
#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(Age))
print(type(current_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
first_name_len= len(first_name)
last_name_len= len(last_name)
com = first_name_len > last_name_len
print(com)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff
var_diff= num_one - num_two 
print(var_diff)

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

# Divide num_one by num_two and assign the value to a variable division
var_div= num_one / num_two
print(var_div)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
var_rem= num_one % num_two
print(var_rem)

# Calculate num_one to the power of num_two and assign the value to a variable exp
var_exp = num_one ** num_two
print(var_exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division= num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters

from cmath import pi
r = 30 
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle= pi * (r ** 2)
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * r
print(circum_of_circle)

# Take radius as user input and calculate the area.
r = input('Enter a number: ')
area = pi * (r ** 2)
print(area)


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name_ = input('Enter first name: ')
last_name_= input('Enter lastname:')
country_ = input('Enter country name:')
userAge= input('Enter user age:')

print(first_name_)
print(last_name_)
print(country_)
print(userAge)

help('keywords')