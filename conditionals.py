# Day 9 of 30 Day of Python
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""

# User input age
print('#1')
age = int(input('Enter your age:'))

if age >= 18:
    print('You are old enough to drive')
else:
    young_age = 18 - age
print('Wait for {} before you can drive'.format(young_age))


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
"""Enter your age: 30
You are 5 years older than me."""

# # users input ages
print('#2')
my_age = int(input('Enter my age:' ))
your_age = int(input('Enter your age: '))
year = your_age - my_age
years = your_age - my_age

if my_age > your_age or year == 1:
    print(('You are {} year older than me'.format(year)))

elif my_age > your_age or years > 1:
    print(f'You are {years} years older than me')


else:
    my_age == your_age
    print('We are same age!!!')


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
"""Enter number one: 4
Enter number two: 3
4 is greater than 3"""
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

if a > b:
    print('a is greater than b')

elif a < b:
    print('a is smaller than b')

else:
    print('a is equal b')

# Write a code which gives grade to students according to theirs scores:
"""80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

# grades = int(input('Enter student grade: '))

if grades >= 80:
    print('A')
elif grades >= 70:
    print("B")
elif grades >= 60:
    print('C')
elif grades >= 50:
    print('D')
else:
    print('F')


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = str(input('Enter a month: '))

if month == 'September':
    print('The season is Autumn')
elif month == 'October':
    print('The season is Autumn')
elif month == 'November':
    print('The season is Autumn')
elif month == 'December':
    print('The season is Winter')
elif month == 'January':
    print('The season is Winter')
elif month == 'February':
    print('The season is Winter')
elif month == 'March':
    print('The season is Spring')
elif month == 'April':
    print('The season is Spring')
elif month == 'May':
    print('The season is Spring')
else:
    print('The season is Summer')

# The following list contains some fruits:

"""fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

"""


fruit = str(input('Enter a fruit:'))
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit not in fruits:
   fruits.append(fruit)
   print(fruits)

else:
    print('The fruit already exist')

# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

# if 'skills' in person:
#     print(person['skills'][2])
print('2')

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result
if 'skills' in person.keys():
    print("True")
    if 'Python' in person['skills']:
        print('Python is in skills list')

# If the person is married and if he lives in Finland, print the information in the following format
#    Asabeneh Yetayeh lives in Finland. He is  married.
if person['is_marred'] == True and person['country'] == 'Finland':
    print('{} {} lives in {}.He is married'.format(person['first_name'], person['last_name'], person['country']))

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills_set = set(person['skills'])
print(skills_set)

if ('JavaScript', 'React') == skills_set:
        print('He is a Front-end Developer')
elif ('Node', 'Python', 'MongoDB') == skills_set:
    print('He is a Back-end developer')
elif ('React', 'Node','MongoDB') in skills_set:
    print('He is a Full Stack Engineer')
else:
    print('Unknown Title')
