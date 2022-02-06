# Day 6 of 30 Day of Python Challenge
# Create an empty tuple
print('#1')

tple = ()

print(tple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
print('#2')

tpl_bro= ('Chidiebere', 'David', 'Moses')
tpl_sis= ('Chinonso', 'Chinaka', 'Chigozie', 'Uju', 'Amarachi')

# Join brothers and sisters tuples and assign it to siblings
print('#3')
tpl_sib= tpl_bro + tpl_sis
print(tpl_sib)

# How many siblings do you have?
print('#4')
print(len(tpl_sib))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print('#5')
tpl_list = list(tpl_sib)
print(tpl_list)

parents = 'Dad', 'Mum'
tpl_list.append(parents)
print(tpl_list)

tpl_fam = tuple(tpl_list)
print(tpl_fam)

# Unpack siblings and parents from family_members
# print('#6')
*siblings, parents = tpl_list

print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
print('#7')
fruits = ('avocado', 'banana','mango', 'berries')
vegetable= ('cumcumber', 'spinach', 'cabbage')
ani_prod= ('milk', 'meat', 'beef')

food_stuff_tp= fruits + vegetable + ani_prod
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
print('#8')
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print('#10')
print(len(food_stuff_lt))
print(len(food_stuff_lt) // 2)
print(food_stuff_lt[4])


# Slice out the first three items and the last three items from food_staff_lt list
print('#11')
first_three = food_stuff_lt[4:8]
print(first_three)

# Delete the food_staff_tp tuple completely
print('#12')
del food_stuff_tp



# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country
print('#13')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
check_est = 'Estonia' in nordic_countries
print(check_est)

check_ice = 'Iceland' in nordic_countries
print(check_ice)





