print('Task 19!')
print()

print('1.')
def q1(*a):
    return sum(a)
print(q1(1, 3, 4, 6))
print()

print('2.')
def q2(**a):
    total = 1
    for i in a.values():
        total *= i
    return total
print(q2(a=3, f=7))
print()

print('3.')
def q3(a, **b):
    total = a
    for i in b.values():
        total += i
    return total
print(q3(4, h=4, fg=436))
print()

print('4.')
def q4(*a, b=2, c=7):
    total = 1
    for i in a:
        total *= i
    return total * b * c
print(q4(4, 5, 2))
print()

print('5.')
def q5(*a, **b):
    t1 = 0
    t2 = 0
    for i in a:
        t1 += i
    for s in b.values():
        t2 += s
    return t1 + t2
print(q5(4, 6, 2, f=25, dfg=2))