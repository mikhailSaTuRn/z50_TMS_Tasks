import re

print('Task 29!')
print()

print('1.')
print(re.match("^a\d+c$", 'a23c') is not None)
print()

print('2.')
print(re.match("^a\d*c$", 'ac') is not None)
print()

print('3.')
def q3(email):
    s = re.match('^(.+)@.+$', email)
    ss = s is not None
    if ss != True:
        raise Exception('Понимаю только email')
    else:
        login1 = s.groups()
    return login1[0]
print(q3('manager@zhizni.net'))
print()

print('4.')
s = '<n>smth<n>'
ss = re.match('^<\w+>(\w+)<\w+>$', s).groups()
print(ss[0])
print()

print('5.')
def minn(tt):
    s = re.match('^\d{4}-\d{2}-\d{2}\s\d{2}:(\d\d):\d{2}$', tt)
    ss = s is not None
    if ss != True:
        return 'не понимаю'
    else:
        minutes = s.groups()
        return minutes[0]
print(minn("2018-01-09 12:32:04"))
print()

print('6.')
def calc(s):
    ss = re.match("^([+-]?\d+.\d+|[+-]?\d+)\s?(\+|-|\*|/)\s?([+-]?\d+.\d+|[+-]?\d+)$", s)
    ch = ss is not None
    if ch != True:
        return 'не понимаю. Пробуй ещё'
    else:
        l = ss.groups()
    if re.match('^\d+.\d+$', l[0]) is not None:
        a = float(l[0])
    else:
        a = int(l[0])
    if re.match('^\d+.\d+$', l[2]) is not None:
        b = float(l[2])
    else:
        b = int(l[2])
    if l[1] == '+':
        return a + b
    elif l[1] == '-':
        return a - b
    elif l[1] == '/':
        return a / b
    elif l[1] == '*':
        return a * b
print(calc('4.21 / -5'))