# Day 8 of 30 Day of Python Challenge
# Create an empty dictionary called dog
print('#1')
dog = {}
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
print('#2')
dog= {'name': 'Segun', 'dog_colour': 'black', 'legs': 4,'age': 2}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print('#3')
student = {'first_name': 'Patience', 'last_name': 'Isaac', 'gender': 'Female', 'age': 20, 'marital status': 'Single', 'skills': ['HTML', 'Java', "Python", 'SQL'], 'country': 'Nigeria', 'address': 'Lagos'}

print(student)

# Get the length of the student dictionary
print('#4')
print(len(student))

# Get the value of skills and check the data type, it should be a list
print('#5')
skills_get = student.get('skills')
print(type(skills_get))

# Modify the skills values by adding one or two skills
print('#6')
student['skills'].append('Javascript')
print(student)

# Get the dictionary keys as a list
print('#7')
print(student.keys())

# Get the dictionary values as a list
print('#8')
print(student.values())

# Change the dictionary to a list of tuples using items() method
print('#9')
print(student.items())

# Delete one of the items in the dictionary
print('#10')
# print(student.popitem())
student.popitem()
print(student)

# Delete one of the dictionaries
print('#11')
del student
