n = [1,2,3,4,5,6,7,8,9,10]


is_prime = lambda x: x if x == 1 else ('Prime' if 0 not in map(lambda z: x % z, range(2, x)) else x)
print(list(map(is_prime, n)))


def remove_prime(our_list):
    prime_lambda = lambda x: x if x == 1 else (None if 0 not in map(lambda z: x % z, range(2, x)) else x)
    return list(filter(None, map(prime_lambda, our_list)))


print(remove_prime(n))