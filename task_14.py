print('Task 14')
print()

print('1.')
def q1(a):
    total = 0
    for i in a:
        total += i
    print(total)
q1([1, 1, 2, 3, 5, 8])
print()

print('2.')
def q2(a):
    a1 = []
    for i in a:
        a1.append(i / 2)
    print(a1)
q2([1, 1, 2, 3, 5, 8])
print()

print('3.')
def q3(a):
    total = 0
    for i in a:
        total += 1
    print(total)
q3([1, 1, 2, 3, 5, 8])
print()

print('4.')
def q4(a, b):
    count = 0
    for i in a:
        count += 1
        if i == b:
            print('True')
            break
        elif count >= len(a):
            print('False')
q4([1, 1, 2, 3, 5, 8], 4)
print()

print('5.')
def q5(a):
    total = 0
    for i in a:
        total += i
    print(total / 2)
q5([1, 1, 2, 3, 5, 8])
print()

print('6.')
def q6(a):
    maxi = a[0]
    for i in a:
        if i > maxi:
            maxi = i
    print(maxi)
q6([1, 1, 2, 3, 5, 8])
print()

print('7.')
def q7(a):
    mini = a[0]
    for i in a:
        if i < mini:
            mini = i
    print(mini)
q7([1, 1, 2, 3, 5, 8])
print()

print('8.')
def q8(a):
    a1 = []
    for i in a:
        if i % 2 == 0:
            a1.append(i)
    print(a1)
q8([1, 1, 2, 3, 5, 8])
print()

print('9.')
def q9(a):
    a1 = []
    for i in a:
        if i % 2 != 0:
            a1.append(i)
    print(a1)
q9([1, 1, 2, 3, 5, 8])
print()

print('10.')
def q10(a, b):
    a1 = []
    for i in a:
        for s in b:
            if i == s:
                a1.append(i)
    print(a1)
q10([1, 1, 2, 3, 5, 8, 42], [4, 8, 15, 16, 23, 42])
print()

print('11.')
def q11(a, b):
    a1 = []
    for i in a:
        flag = False
        for s in b:
            if i == s:
                flag = True
                break
        if not flag:
            a1.append(i)
    print(a1)
q11([1, 1, 2, 3, 5, 8, 42], [4, 8, 15, 16, 23, 42])
print()

print('11.2.')
def q112(a, b):
    total = 0
    for i in range(b):
        total += a
    print(total)
q112(2, 4)
print()

print('12.')
def q12(a, b):
    total = 1
    for i in range(b):
        total *= a
    print(total)
q12(4, 3)
print()

print('13.')
def q13():
    for i in range(1, 11):
        for s in range(2, 11):
            print(i, '*', s, '=', i*s)
q13()
print()

print('14.')
def q14(a):
    x = ' ' * 3 + str(a[0])
    l = len(str(a[0]))
    s = len(x)
    for i in a:
        xy = ' ' * (s - len(str(i))) + str(i)
        print(xy)
q14([123, 1, 27, 3, 55, 8])
print()

print('15.')
def q15():
    score = 0
    x = 0
    y = 0
    while score < 11:
        print('У вас', str(score), 'очков.')
        x = int(input('Введите первое число: '))
        if x == -1:
            break
        y = int(input('Введите второе число: '))
        if y == -1:
            break
        res = x * y
        print('Сколько будет', str(x), '*', str(y), '?: ', end='')
        ans = int(input())
        if res == ans:
            print('Верно')
            score += 1
        else:
            print('Неверно')
    return "Пока."


#print(q15())
print()

print('16.')
def q16(a):
    maxprev = a[0]
    maxmax = a[0]
    for i in a:
        if i > maxmax:
            maxprev = maxmax
            maxmax = i
    print(maxmax)
    print(maxprev)
q16([13, 44, 44, 7, 2, 5])
print()

print('17.')
def q17(n):
    for i in range(n):
        print('*' * n)
q17(4)
print()

print('18.')
def q18(a):
    print('*' * a)
    for i in range(a-2):
        print('*', '' * (a-2), '*')
    print('*' * a)
q18(4)
print()

print('19.')
def q19(a):
    for i in range(a//2):
        print('* ' * a)
        print(' *' * a)
    if a % 2 == 1:
        print('* ' * a)
q19(5)
print()

print('20.')
def q20(a, b):
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)
q20(3, 15)
print()

print('21.')
print('Original variant:')
def q21(a):
    total = 1
    for i in range(2, a+1):
        total *= i
    return total
print(q21(5))
print('Alternative variant')
import math
def q21(a):
    return math.factorial(a)
print(q21(5))
print()

print('22.')