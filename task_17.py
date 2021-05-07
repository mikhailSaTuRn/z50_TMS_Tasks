print('Task 17!')
print()

print('13.1')
def q131(a):
    try:
        if a <= 34:
            print('Misha')
        else:
            print('Natasha')
    except Exception as e:
        print("Я принимаю только числа")
#q131('f')
print()
def q131i(a):
    if isinstance(a, int):
        if a <= 34:
            print('Misha')
        else:
            print('Natasha')
    else:
        raise Exception("Я принимаю только числа")
#q131i('f')
print()

print('13.2')
def q132(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a + b == 5:
            return (a + b) / 2
        else:
            return a + b
    else:
        raise Exception("Я принимаю только числа")
print(q132(2, 3))
print()

print('13.3')
def q133(a):
    if isinstance(a, str):
        if len(a) > 5:
            raise Exception('строка сильно большая , я устал')
        else:
            return a
    else:
        raise Exception("Я печатаю только строки")
#print(q133(123333))
print()

print('13.5')
def q135(i, s):
    print(str(i) + ' * ' + str(s) + ' = ')
    x = input()
    while True:
        try:
            if int(x) == i * s:
                print('верно')
            else:
                print('неверно')
            break
        except Exception as e:
            print("Try again")
            x = input()
#q135(2, 3)
print()

print('13.8')
def q138(a):
    if a == 'Вася' or a == 'Петя':
        return 'Привет братаны'
    elif a == 'Толик':
        return 'Поделись на нолик'
    else:
        raise Exception('Я тебя не знаю')
#print(q138('Tolik'))
print()

print('14.1')
def q141(a):
    total = 0
    for i in a:
        try:
            total += i
        except Exception as e:
            #print('skip')
            continue
    return total
#print(q141([3, 7, 1, '1', '1', 1]))
print()

print('14.5')
def q145(a):
    total = 0
    if a == []:
        raise Exception('Не могу посчитать среднее для пустого списка')
    for i in a:
        try:
            total += i
        except Exception as e:
            # print('skip')
            continue
    return total / len(a)
#print(q145([3, 7, 1, 1, 1, 1]))
print()

print('14.6')
def q146(a):
    l1 = []
    for p in a:
        if isinstance(p, int):
            l1.append(p)
    if l1 == []:
        raise Exception('В списке нет чисел')
    maxi = l1[0]
    for i in l1:
        try:
            if i > maxi:
                maxi = i
        except Exception as e:
            # print('skip')
            continue
    return maxi


print('Максимальное число:', q146(['fgj', 'dhjdjh', 0]))
print()

print('14.8')
def q148(a):
    l1 = []
    for i in a:
        try:
            if i % 2 == 0:
                l1.append(i)
        except Exception as e:
            # print('skip')
            continue
    return l1
#print(q148([3, 7, 1, '4', 1, 10]))
print()