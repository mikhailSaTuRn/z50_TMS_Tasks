print("Task 38!")
print()

import pandas
info = pandas.read_csv("info.csv")
marks = pandas.read_csv("marks.csv")

print('1.')
info1 = info.merge(marks, left_on='id', right_on='id2', how='left')
count_nan = info1[(info1['math'] == 'nan') & (info1['reading'] == 'nan') & (info1['writing'] == 'nan')]
len(count_nan.shape)
print(count_nan.shape)