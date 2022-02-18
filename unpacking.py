#DAy 17 of 30 day of Python Challenge
''''names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic, es, ru = names
print(nordic)
print(es)
print(ru)
print(nordic, es, ru)