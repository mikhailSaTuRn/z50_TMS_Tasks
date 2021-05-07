import re

print('Task 28!')
print()

print('1.')
s = "HB2030706"
print(re.match("^[HBMP][HBMP]\d{7}$", s) is not None)
print()

print('2.')
ss = "Добрый день дорогой юзер"
print(re.match("^(Привет.*|Салют.*|Добрый.*)$", ss) is not None)
print()

print('3.')
sss = "-25.624 / -4"
print(re.match("^[+-]?(\d+.\d+|\d+)\s?(\+|-|\*|/)\s?[+-]?(\d+.\d+|\d+)$", sss) is not None)