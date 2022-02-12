# Day 12 of 30 Day of Python Challenge
'''Writ a function which generates a six digit/character random_user_id.
'''

import random
import string

def random_user_id():
    letters = string.ascii_lowercase
    user_id = ''.join (random.choice(letters) for i in range(6))
    return user_id

print(random_user_id())

# import random 
# import string

# def user_id_gen_by_user():
#     num_id = int(input('Enter a number: '))
#     num_char = int(input('Enter a number: '))
#     letters = string.ascii_letters
#     for i in range(num_char):
#          user_id = ''.join(random.choice(letters) for i in range(num_char))
#     return user_id

# print(user_id_gen_by_user())

'''Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
'''
import random
import string
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)

    return [r,g,b]
print(rgb_color_gen())

'''Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).'''
print('#3')
import random
def list_of_hexa_colors():
    color = []
    for j in range(5):
        hexa = ['#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        color.append(hexa)
    return color
print(list_of_hexa_colors())

'''Write a function list_of_rgb_colors which returns any number of RGB colors in an array.'''
print(4)

import random
def list_of_rgb_colors():
    color = []
    for i in range(5):
         r = random.randint(0,255)
         g = random.randint(0,255)
         b = random.randint(0,255)

         color.append([r,g,b])

    return color
print(list_of_rgb_colors())

'''Write a function generate_colors which can generate any number of hexa or rgb colors.'''
print(5)
import random
def generate_colors(hexa, n):
    color = []
    for i in range(n):
        hexa = ['#'+ ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        color.append(hexa)
    return ('hexa',color)
print(generate_colors('hexa', 3))

'''Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list'''
print(6)
import random
def shuffle_list(n):
    l = list(range(n))
    lr = random.sample(l,len(l))
    return lr
print(shuffle_list(10))

'''Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.'''
import random
def ran_num(n):
    l = set(range(n))
    return l

print(ran_num(10))

