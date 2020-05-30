l1 = [1,2,3,4,5,6,7]
l2 = [1,1]
# USE COMMENTED PRINT TO SEE THE VALUES ADDED #


def slider_adder(longer_list, shorter_list):
    s = 0
    if len(longer_list) <= len(shorter_list):
        longer_list, shorter_list = shorter_list, longer_list

    for index, items in enumerate(longer_list):
        i = index
        for elements in shorter_list:
            # print(f'i={i}, shorter list ={elements}, longer list = {longer_list[i]}')
            s = s + elements+longer_list[i]
            i+=1
            # print(f'i after increment {i}')
            # print(f'sum = {s}')
        if i == len(longer_list):
            break

    return s


print(slider_adder(l1, l2))