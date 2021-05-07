import re
print('Task 27!')
print()

print('1.')
print(re.match("^ $", ' ') is not None)
print()

print('2.')
s = '9'
print(re.match("^\d$", s) is not None)
print()

print('3.')
s = '4f'
print(re.match("^\d\d$", s) is not None)
print()

print('4.')
print(re.match("^\s\s\s$", '   ') is not None)
print()

print('5.')
print(re.match("^a\dv$", 'a8v') is not None)
print()