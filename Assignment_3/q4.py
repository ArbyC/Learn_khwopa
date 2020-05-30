# Squares of first 100 Prime numbers#
prime = []
for i in range(2, 700):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i ** 2)
    if len(prime) == 100:
        break
print(prime)