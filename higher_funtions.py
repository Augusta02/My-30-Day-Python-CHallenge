# Day 14 of 30 Day of Python Challenge
from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''Explain the difference between map, filter, and reduce.
 map() takes in two parameters, a function and an iterable and retruns an iterable. 
 filter() also takes in two parameters, a function and an iterable and returns an iterable too, it identifies the speficied function which returns a boolean for each item in the iterable.
 reduce() like map and filter takes in two parameters but returns one value'''

'''Explain the difference between higher order function, closure and decorator
 higher order functions in python takes in a function as a parameter and also returns funtion as a value
 Closure allows a nested funtion to access an outer scope of the enclosing function.
 Decorator is a design pattern that allows one to modify an existing object without modifying its structure'''

'''Use for loop to print each country in the countries list.'''
print('#4')
for i in countries:
    print(i)

'''Use for to print each name in the names list.'''
print('#5')
for i in names:
    print(i)

''''Use for to print each number in the numbers list.'''
print('#6')
for i in numbers:
    print(i)

'''Use map to create a new list by changing each country to uppercase in the countries list'''
print('#7')
new_list = map(lambda countries: countries.upper(), countries)
print(list(new_list))

'''Use map to create a new list by changing each number to its square in the numbers list'''
print('#8')
def square_num(x):
    return x ** 2
new_num = map(square_num, numbers)
print(list(new_num))

'''Use map to change each name to uppercase in the names list'''
print('#9')
new_names = map(lambda names: names.upper(), names)
print(list(new_names))

'''Use filter to filter out countries containing 'land'.'''
print('#10')
def new_countries(countries):
    for x in countries:
        if 'land' in x:
            return True
        else:
            return False

new_= filter(new_countries, countries)
print(list(new_))


'''Use filter to filter out countries having exactly six characters.'''
print('#11')
def six_countries(countries):
    if len(countries) == 6:
        return True
    else:
        return False
long_countries = filter(six_countries, countries)
print(list(long_countries))

'''Use filter to filter out countries containing six letters and more in the country list.'''
print('#12')
def more_countries(countries):
    if len(countries) >= 6:
        return True
    else:
        return False
fil_countries = filter(more_countries, countries)
print(list(fil_countries))

'''Use filter to filter out countries starting with an 'E'''
print('#13')
def vowel_countries(countries):
    for i in countries:
        if 'E' in i:
            return True
        else:
            return False
non_vowel_countries = filter(vowel_countries, countries)
print(list(non_vowel_countries))

'''Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))'''



'''Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items'''
# def get_strings_lists(x):
#   new_strings = ' '. join(map(str, x))
# print(list(get_strings_lists([1,2,3,4,5])))

'''Use reduce to sum all the numbers in the numbers list.'''
print('#16')
def sum_all_num(x,y):
    return x + y
total =reduce (sum_all_num, numbers)
print(total)

'''Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries'''
def conc_countries(countries):
    for i in countries:
        i + i
    return i
print(conc_countries(countries))
  

# countries_= reduce(conc_countries, countries)
# print('{} are North European countries'.format(countries_))  return i


list_countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
def categorize_countries(list_countries):
    y= []
    for i in list_countries:
        if 'land' ==  i:
            y.append(i)
        return y
       
print(categorize_countries(list_countries))

'''
Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.'''
print()