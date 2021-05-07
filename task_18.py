print('Task 18!')
print()

print('1.')
def q1(a, b=7):
    return a * b
print(q1(3))
print(q1(2, 4))
print()

print('2.')
def q2(a, b=[3, 1, 7]):
    t1 = 0
    t2 = 0
    for i in a:
        t1 += i
    for s in b:
        t2 += s
    return t1 + t2
print(q2([5, 3, 8]))
print(q2([1, 7, 6], [5, 2, 7]))
print()

print('3.')
def q3(a, b=3, c={'x': 11, 'y': 12, 'z': 13, 'divisor': 3}):
    return (a + b) / c['divisor']
print(q3(12))
print(q3(13, 5))
print(q3(11, 1, c = {'divisor': 4}))