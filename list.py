# Declare an empty list
print('#1')

lst= list()
print(lst)

# Declare a list with more than 5 items
print('#2')
new_lst= ['Data Science', 'Data Engineering', 'Data Analytics', 'Machine Learning', 'Artificial Intelligence', 'Deep Learning', 'Neural Networks']
# print(new_lst)

lst = list(new_lst)
print(lst)

# Find the length of your list
print('#3')

print(len(lst))


# Get the first item, the middle item and the last item of the list
print('#4')
lst_first = lst[0:7:3]
print(lst_first)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print('#5')
mixed_data_types= ['Augusta', 25, 165, 'Single', '50 Osuji Street Agaye']
print(mixed_data_types)


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

print('#6')
it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


#Print the list using print()

print('#7')
print(it_companies)


# Print the number of companies in the list
print('#8')
print(len(it_companies))

# Print the first, middle and last company
print('9')
com_list= it_companies[0:7:3]
print(com_list)

# Print the list after modifying one of the companies
print('#10')
it_companies[-2] = 'Twitter'
print(it_companies)

# Add an IT company to it_companies
print('#11')
it_companies.append('Airbnb')
print(it_companies)

# Insert an IT company in the middle of the companies list
print('#12')
# print(len(it_companies))
it_companies.insert(3, 'Meta')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print('#13')
print(it_companies[3].upper())


# Join the it_companies with a string '#;  
print('#14')
join_lst = '#'.join(it_companies)
print(join_lst)


# Check if a certain company exists in the it_companies list.
print('#15')
print('Meta' in it_companies)

# Sort the list using sort() method
print('#16')
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
print('#17')
it_companies.reverse()
print(it_companies)


# Slice out the first 3 companies from the list
print('#18')
slice_= it_companies[3:]
print(slice_)

# Slice out the last 3 companies from the list
print('#19')
rev_slice  = slice_[:-3]
print(rev_slice)

# Slice out the middle IT company or companies from the list
print('#20')
mid_slice= rev_slice[::2]
print(mid_slice)

# Remove the first IT company from the list
print('#21')
it_companies.remove('Twitter')
print(it_companies)

# Remove the middle IT company or companies from the list
print('#22')
it_companies.remove('Google')
print(it_companies)

# Remove the last IT company from the list
print('#23')
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
# print('24')
# it_companies.clear()
# print(it_companies)

# Destroy List
# del it_companies
# print(it_companies)

# Join the following lists:
print('#25')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("#26")
# Sort the list and find the min and max age
ages.sort()
print(ages)

print(min(ages))
print(max(ages))


# Add the min age and the max age again to the list
print('#27')
ages.append(19)
print(ages)

ages.append(26)
print(ages)


# Find the median age (one middle item or two middle items divided by two)
print('#28')

print(ages)
ages.sort()
print(len(ages))
mid = len(ages) // 2

print(mid)

# Find the average age (sum of all items divided by their number
print('#29')

avg_sum = sum(ages) // 2
print(avg_sum)

# Find the range of the ages (max minus min)
print('#30')

age_max = max(ages)
age_min = min(ages)
print(age_max, age_min)
age_range = age_max - age_min
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
print('#31')

comp_age = abs(age_min - avg_sum) > abs(age_max - avg_sum)

print(comp_age)


countries = [
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

# Find the middle country(ies) in the countries list
print('#33')
mid = len(countries) // 2
print(mid)

print(countries[96])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print('#34')
first_half = countries[:96]
print(first_half)

second_half =countries[96:]
print(second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries
new_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
Ch, Ru, US, *scandic = new_countries
print(Ch)






