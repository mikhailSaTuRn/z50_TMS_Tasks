from math import factorial
from json import *
import statistics

print('Average of list [345, 536, 234]:')
print(statistics.mean([345, 536, 234]))
print()
print('Factorial of 5:')
print(factorial(5))
print()
print('Json dumps:')
data = []
a = 'foo'
data.append(a)
b = {'bar': ['baz', None, 1.0, 2], 'key': 'value', 10: 'ten'}
data.append(b)
c = [3, 4, 5, 6]
data.append(c)
json_data = dumps(data, indent=4)
print(json_data)
print(json_data[7:10])
data = loads(json_data)
print(data[0])

print('2.')
print('установил 2.9.3')
from jinja2 import Environment
print()

print('3.')
print('done')
print()

print('4.')
print('done')
from django.http import HttpResponse
print()