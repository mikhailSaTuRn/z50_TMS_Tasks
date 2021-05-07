print('Task 20!')
print()

print('1.')
def q1(a, b, c=2, d=3):
    return a + b + c + d

req_arg = (1, 3, 4, 6)
print(q1(*req_arg))
print()

print('2.')
def q2(a=1, f=4):
    total = 1
    return a * total * f

kw = {'a': 3, 'f': 7}
print(q2(**kw))
print()

print('3.')
def q3(a, h=45, fg=235):
    return a + h + fg

kw = {'h': 4, 'fg': 436}
print(q3(4, **kw))
print()

print('4.')
def q4(a, a1, b=2, c=7):
    return a * a1 * b * c
args = (2, 3)
kwar = {'b': 4, 'c': 5}
print(q4(*args, **kwar))
print()

print('5.')
def q5(a, b, c=3, d=4):
    return a + b + c + d
args = (2, 8)
kwar = {'c': 12, 'd': 8}
print(q5(*args, **kwar))