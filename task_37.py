print('Task 37!')
print()

import pandas
df = pandas.read_csv('titanic.csv')
print('1.')
print(df.columns)
print()

print('2.')
count = len(df['Name'])
print('Number of people:', count)
print()

print('3.')
count_m = len(df[df['Sex'] == 'male'])
count_f = len(df[df['Sex'] == 'female'])

print('Number of males:', count_m)
print()

print('4.')
count_surv = len(df[df['Survived'] == 1])
pc = count_surv * 100 / count
print('Survived:', str(pc) + '%')
print()

print('5.')
if count_f > count_m:
    print("Women's power!")
else:
    print("Men's power!")
print()

print('6.')
df1 = df[(df['Survived'] == 1) & (df['Sex'] == 'male')]
count_surv_m = df1.shape[0] * 100 / count_surv
print(count_surv_m)
print()

print('7.')
count1 = len(df[(df['Pclass'] == 1)])
count2 = len(df[(df['Pclass'] == 2)])
count3 = len(df[(df['Pclass'] == 3)])

df_surv1 = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]
df_surv2 = df[(df['Pclass'] == 2) & (df['Survived'] == 1)]
df_surv3 = df[(df['Pclass'] == 3) & (df['Survived'] == 1)]
count_surv1 = df_surv1.shape[0]
count_surv2 = df_surv2.shape[0]
count_surv3 = df_surv3.shape[0]
pr1 = count_surv1 * 100 / count1
pr2 = count_surv2 * 100 / count2
pr3 = count_surv3 * 100 / count3

if pr3 < pr1 > pr2:
    print('Abramovichs are winners!')
elif pr1 < pr2 >pr3:
    print('Timberlands are winners!')
else:
    print('Hobos are winners!')
