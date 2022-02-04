# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('#1')
str_conc= ('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')
print(str_conc)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('#2')
str_ = ('Coding' + ' ' + 'For' + ' ' + 'All')
print(str_)

# Declare a variable named company and assign it to an initial value "Coding For All".
print('#3')
company= 'Coding For All'

# Print the variable company using print().
print('#4')
print(company)

# Print the length of the company string using len() method and print().
print('#5')
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print('#6')
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print('#7')
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('#8')
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice out the first word of Coding For All string.
print('#9')
str_slice = company[1:]
print(str_slice)


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('#10')
str_find= company.find('Coding')
print(str_find)

str_r = company.rfind('Coding')
print(str_r)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('#11')

str_rep= company.replace('Coding', 'Python')

print(str_rep)

# Change Python for Everyone to Python for All using the replace method or other methods.
print('#12')

var = 'Python For Everyone'
var_ = var.replace('Python For Everyone', 'Python For All')
print(var_)

# Split the string 'Coding For All' using space as the separator (split()) 
print('#13')
str_new = 'Coding For All'
print(str_new.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print('#14')
big_names= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(big_names.split(','))


# What is the character at index 0 in the string Coding For All
print('#15')
print(str_new[0])

# What is the last index of the string Coding For All.
print('#16')

print(str_new[-1])

# What is the last index of the string Coding For All.
print('#17')

print(str_new[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('#18')
print(var)
print(len(var))
print(var[0:20:9])

# Create an acronym or an abbreviation for the name 'Coding For All'.
print('#19')
print(str_new)
print(len(str_new))
print(str_new[0:15:7])

# Use index to determine the position of the first occurrence of C in Coding For All.
print('#20')
print(str_new.find('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print('#21')
print(str_new.find('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('#22')
print(str_new.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('#23')
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('#24')
print(sentence.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('#25')
print(sentence[31:55])

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('#26')
print(sentence.find('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("#27")
print(sentence[31:55])


# Does ''Coding For All' start with a substring Coding?
print('#28')
print(str_new.startswith('Coding'))


# Does 'Coding For All' end with a substring coding?
print('#29')
print(str_new.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# print('#30')
# new_var = '   Coding For All      ' 
# print(new_var)


# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

# print('#31')
# num_var = '30DaysOfPython'
# alp_var= 'thirty_days_of_python'

# print(num_var.isidentifier())
# print(alp_var.isidentifier())


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print('#32')
pyt_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(pyt_lib))


# Use the new line escape sequence to separate the following sentences.
print('#33')
new_line= 'I am enjoying this challenge.\nI just wonder what is next.'
print(new_line)

# Use a tab escape sequence to write the following lines

print('#34')
str_title= 'Name\tAge\tCountry\tCity'
str_ans= 'Asabeneh\t250\tFinaland\tHelsinki'

print(str_title.expandtabs(10))
print(str_ans.expandtabs(10))


# Use the string formatting method to display the following:
print('#35')
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

print('The area of a circle with radius {} is {:.2f} meters square'.format(radius, area))

# Make the following using string formatting methods:
"""8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""
a= 8
b= 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')