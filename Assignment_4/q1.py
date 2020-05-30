# Star Pattern python way #


def pattern(no_of_rows=5):
    [print('*'*i) for i in range(1, no_of_rows+1)]


pattern()

# Star Pattern classic way #


def pattern_classic(no_of_rows=5):
    for i in range(1, no_of_rows+1):
        for j in range(i):
            print('*', end='')
        print('')


pattern_classic()