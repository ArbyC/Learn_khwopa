# Removed duplicates #
in_list = input('Enter list with duplicates seperate with space:').split(' ')
# USE IF ORDER MATTERS #
empty_list = []
for items in s:
    if items not in a:
        empty_list.append(items)
print(empty_list)

# USE IF ORDER DOESN'T MATTER #
new_list = list(set(in_list))
print(new_list)