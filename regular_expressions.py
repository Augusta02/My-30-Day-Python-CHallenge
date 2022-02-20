# Day 18 of 30 day of Python Code
import re
from collections import Counter

'''What is the most frequent word in the following paragraph?'''
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'
# matches = re.findall('I', paragraph)
# print(len(matches), 'I')


'''Write a pattern which identifies if a string is a valid python variable'''
regex = '^ [A - Za -z_][A - Za-z0-9_]*'
def check(string):
    if (re.search(regex, string)):
        print('True')
    else: 
        print('False')
    
print(check('first-name'))

'''Clean the following text. After cleaning, count three most frequent words in the string.'''
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
regex = r'[^0-9a-zA-Z]+'
clean_text = re.sub(regex,'', sentence)
# clean_string = ' '. join(clean_text)
print(clean_text)
