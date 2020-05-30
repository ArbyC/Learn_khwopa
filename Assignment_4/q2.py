price = [('orange', 100), ('watermelon', 200), ('papaya', 300)]


def convert(prices):
    print('Next function')
    return dict(items for items in prices)


print(convert(price))