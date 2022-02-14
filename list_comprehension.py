# Day 13 of 30 Day of Python Code
'''Filter only negative and zero in the list using list comprehension'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i <= 0]
print(negative_numbers)

'''Flatten the following list of lists of lists to a one dimensional list '''
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list = [i for num in list_of_lists for x in num for i in x]
print(new_list)

'''Using list comprehension create the following list of tuples:'''
list_of_tuple= [(i, 1, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_of_tuple)

'''Flatten the following list to a new list:'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [i for country in countries for i in country]

print(new_countries)

'''Change the following list of lists to a list of concatenated strings:'''
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
conc_string = [' '.join(element) for i in names for element in i]
print(conc_string)

'''Write a lambda function which can solve a slope or y-intercept of linear functions.'''
y = lambda m, x, b: m * x + b
print(y(4,2,0.5))