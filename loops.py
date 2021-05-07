#http://www.itmathrepetitor.ru/s-zadachi-s-resheniyami-chisla-i-cikly-2/

print('- = LOOP for = -')
print()

print('1.')
for i in range(10, 21):
    print(i ** 2)
print()

print('2.')
for i in range(35, 87+1):
    s = i % 7
    if s in [1, 2, 5]:
        print(i)
print()

print('3.')
n = 4#int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)
print()

print('4.')
n = 1234
n = str(n)
total = 1
for i in n:
    total *= int(i)
print(total)
print()

print('5.')
n = 123455
n = str(n)
count = 0
for i in n:
    if int(i) % 2 == 0:
        count += 1
print(count)
print()

print('6.')
n = 6787231345
n = str(n)
maxi = int(n[0])
for i in n:
    if int(i) > maxi:
        maxi = int(i)
print(maxi)
print()

print('7.')
for i in range(1059, 9601):
    i = str(i)
    count = 0
    for s in i:
        count += int(s)
    if count == 15:
        print(int(i))
print()

print('8.')
for i in range(2, 99):
    for s in range(1, i+1):
        if i