print('Task 25!')
print()

print('1.')
q1 = lambda x: x + 100
s = list(map(q1, [432, 346, 254, 25]))
print(s)
print()

print('2.')
q2 = lambda x: x % 2 == 1
print(list(filter(q2, [235, 235, 121, 544, 114])))
print()
