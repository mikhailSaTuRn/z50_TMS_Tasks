print('Task 32!')
print()

import random

def some_fn(a, b):
    c = a + b
    return c


def reduce(fn, ls, acc):
    if len(ls) == 0:
        return acc
    else:
        new_acc = fn(ls[0], acc)
        ls_without_first_element = ls[1:]
        result = reduce(fn, ls_without_first_element, new_acc)
        return result
print(reduce(some_fn, [36, 364, 23], 5468))

