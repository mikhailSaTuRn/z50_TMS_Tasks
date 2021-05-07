print('Task 24!')
print()

print('1.')
def cap(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        d = result.capitalize()
        return d
    return wrapper

@cap
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]

print(swap_words('привет мир'))
print()

print('2.')
def smth(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        result1 = fn(result)
        return result1
    return wrapper

@smth
def mult_on_2(ls):
    result = []
    for x in ls:
        result.append(x * 2)
    return result

print(mult_on_2([3, 43, 67, 34]))
print()

print('3.')
import math
def ch(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                print('Нельзя передавать отрицательные числа')
                return -1
            else:
                return fn(*args, **kwargs)
    return wrapper

@ch
def my_sqrt(x):
    return math.sqrt(x)

print(my_sqrt(-3))