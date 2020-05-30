# Merging two input dictionaries#
d1 = input("Enter key=values separate by space:")
d2 = input("Enter key=values separate by space:")
d1 = dict(x.split('=') for x in dict1.split(' '))
d2 = dict(x.split('=') for x in dict2.split(' '))

d1.update(d2)
print(d1)