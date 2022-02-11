#Day 11 of 30 Day of Python Code

'''Declare a function add_two_numbers. It takes two parameters and it returns a sum.'''
from calendar import month
from lib2to3.pytree import convert
from subprocess import ABOVE_NORMAL_PRIORITY_CLASS


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(5,6))

'''Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.'''
def area_of_circle(r):
    PI = 3.142
    area = PI * (r ** 2)
    return area
print(area_of_circle(5))

'''Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.'''

def add_num(*nums):
    sum = 0
    for num in nums:
         sum += num
    return sum
print(add_num(2,3,5,10,11))

'''Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.'''
print('#2')
def convert_celsius_to_fahrenheit(C):
    F = (C * (9/5) + 32)
    return F
print(convert_celsius_to_fahrenheit(34))

'''Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.'''

def check_season(month):
    season = ' '
    season1 = 'Autumn'
    season2 = 'Winter'
    season3 = 'Spring'
    season4 = 'Summer'

    if month == 'September' or month == 'October' or month == 'November':
        season = season1
    elif month == 'December' or month == 'January' or month == 'February':
        season = season2
    elif month == 'March' or month == 'April' or month == 'May':
        season = season3
    else:
        season = season4
    return season

print(check_season('March'))

'''Write a function called calculate_slope which return the slope of a linear equation n'''
def calculate_slope(x1,y1,x2,y2):
    slope = ((y2 - y1) / x2 - x1)
    return slope
print(calculate_slope(8,10,2,6))

'''Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.'''
def solve_quadratic_eqn(a,b,c,x):
    quadratic = (a * (x ** 2) + b * (x) + c)
    return quadratic
print(solve_quadratic_eqn(2,3,1,4))

'''Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list'''
def print_list(x_list):
    fruit_list = ' '
    for i in x_list:
        print(i)
    return fruit_list
    
print(print_list(['banana','orange', 'mango', 'avocado']))

'''Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).'''

def reverse_list(x_list):
    new_list= []
    for i in reversed(x_list):
        new_list.append(i)
    return new_list
print(reverse_list([1,2,3,4,5]))

'''Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items'''

def capitalize_list_items(y_list):
    new_list = []
    for i in range(len(y_list)):
        y_list[i] = y_list[i].capitalize()
        new_list.append(y_list[i])
    return new_list

print(capitalize_list_items(['a','b','c']))


'''Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
'''
def add_items(fruits_list, item):
  fruits_list.append(item)
  return fruits_list
print(add_items(['banana', 'avocado', 'mango'], 'Meat'))

'''Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.'''

def remove_items(fruits_list, item):
    fruits_list.append(item)
    fruits_list.pop()
    return fruits_list
print(remove_items(['banana', 'avocado', 'mango'], 'Meat'))

'''Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.'''
def sum_of_numbers(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum
print(sum_of_numbers(10))

'''Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.'''
def sum_of_odds(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 != 0:
            sum += i
    return sum 
print(sum_of_odds(10))

'''Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
'''
def sum_of_even(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even(10))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    count = 0
    for i in range(n + 1):
        if i % 2 != 0:
            count += 1
    return count
print(evens_and_odds(100))

'''Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number'''
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))

'''Call your function is_empty, it takes a parameter and it checks if it is empty or not'''
def is_empty(n):
    list1 = []
    if len(list1) == 0:
        return 0
    else:
        return 1
print(is_empty([]))

'''Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).'''

def calculate_mean(n):
    mean = sum(n) // len(n)
    return mean
print(calculate_mean([2,2,4,5,8,9,10,10]))

def calculate_median(n):
    median = 0
    len_n = len(n)
    n.sort()
    if len_n % 2 == 0:
        median1 = n[len_n // 2]
        median2 = n[len_n // 2 -1]
        median = (median1 + median2) / 2
    else:
        median = n[len_n // 2] 
    return median
print(calculate_median([2,2,4,5,8,9,10,10]))   

# def calculate_mode(n):
    # n_dict = dict(n)
    # for value in n:
    #     if value in n_dict:
    #         n_dict[value] += 1
    #     else:
    #         n_dict[value] = 1
    #         ()

def calculate_variance(n):
    len_n = len(n)
    mean = sum(n) // len_n
    dev = [(x - mean) ** 2 for x in n]
    variance = sum(dev) / len_n
    return variance
print(calculate_variance([2,2,4,5,8,9,10,10]))

def calculate_std_dev(n):
    len_n = len(n)
    mean = sum(n) // len_n
    dev = [(x - mean) ** 2 for x in n]
    variance = sum(dev) / len_n
    std_dev = variance * 0.5
    return std_dev
    
print(calculate_std_dev([2,2,4,5,8,9,10,10]))


'''Write a function called is_prime, which checks if a number is prime.
'''
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Number is not a prime number"
        else:
            return 'Number is a prime number'
print(is_prime(7))

'''Write a functions which checks if all items are unique in the list.'''
def is_unique(x):
    for i in x:
        if x.count(i) > 1:
            return 'Item is not unqiue'
        else:
            return 'Item is unique'

print(is_unique(['Mon', 'Tue', 'Wed', 'Wed','Mon']))

# def calculate_mode(x):
#     mode = 0
#     for i in x:
#         if x.count(i) > 1:
#             mode = i
#             return mode
#         else:
#             return mode
# print(calculate_mode([2,2,4,5,8,9,10,10]))


def check_type(list_x):
    check = all(isinstance(i, int) for i in list_x)
    return check
print(check_type([2,2,4,5,8,9,10,10]))



            

