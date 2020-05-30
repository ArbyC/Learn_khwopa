# Two list have common element #
list1 = input("Enter first list seperate with ,: ").split(',')
list2 = input("Enter second list seperate with ,: ").split(',')

print(any([items in list1 for items in list2]))