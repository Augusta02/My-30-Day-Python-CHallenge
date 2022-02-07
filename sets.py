# Day 7 of 30 Days of Python Challenge

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print('#1')

print(len(it_companies))

# Add 'Twitter' to it_companies
print('#2')
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
print('#3')
new_companies = ('Airbnb', 'Uber', 'Crosscountry')
it_companies.update(new_companies)
print(it_companies)

# Remove one of the companies from the set it_companies
print('#4')
it_companies.remove('Crosscountry')
print(it_companies)

# What is the difference between remove and discard
print('#5')
# The difference between remove() and discard() is 
# remove() returns an error when its arguement passed in it
# is not contained in the set. 
# discard() does not return an error

# Join A and B
print('#6')
C = A.union(B)
print(C)

# Find A intersection B
print('#7')
D = A.intersection(B)
print(D)

# Is A subset of B
print('#8')
E = A.issubset(B)
print(E)

# Are A and B disjoint sets
print('#9')
F = A.isdisjoint(B)
print(F)

# Join A with B and B with A
print('#10')
G = A.union(B)
H = B.union(A)
print(G)
print(H)

# What is the symmetric difference between A and B
print('#11')
I = A.symmetric_difference(B)
print(I)

# Delete the sets completely
print('#12')
del A
del B

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age)
print(age_set)
com_sets = len(age) > len(age_set)
print(com_sets)

# Explain the difference between the following data types: string, list, tuple and set
# String is a data type that are written in double or single quotes.
# The basically texts or words and they are mutable and indexed
# Lists are ordered and mutable, it can contain various data types. 
# Tuple are ordered and immutable data types. The items in a tuple are correlated 
# and this () are used to create a tuple 
# Sets are unordered and mutable data types. They are similar to that of the mathematical sets.
# {} are used to create a set

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
word = 'I am a teacher and I love to inspire and teach people'
word_split = word.split()
print(word_split)

word_set= set(word_split)
print(word_set)



