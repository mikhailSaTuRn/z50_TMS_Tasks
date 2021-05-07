print('Task 21!')
print()

print('1.')
class Human:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age
kate = Human('female', 30)
sasha = Human('male', 39)
print(sasha.__dict__)
print(kate.__dict__)
print()

print('2.')
class Tree:
    def __init__(self, height, width):
        self.height = height
        self.width = width
birch = Tree(640, 48)
pinetree = Tree(1024, 48)
print(birch.__dict__)
print(pinetree.__dict__)
print()

print('3.')
class House:
    def __init__(self, material, floors):
        self.material = material
        self.floors = floors
house_one = House('wood', 2)
house_two = House('stone', 3)
print(house_one.__dict__)
print(house_two.__dict__)
print()

print('4.')
class Book:
    def __init__(self, author, year):
        self.author = author
        self.year = year
book1 = Book('Pushkin', 1834)
book2 = Book('Karatkevich', 1982)
print(book1.__dict__)
print(book2.__dict__)
print()

print('5.')
class Date:
    def __init__(self, day_week, month):
        self.day_week = day_week
        self.month = month
day2 = Date('Tuesday', 'April')
day5 = Date('Friday', 'April')
print(day2.__dict__)
print(day5.__dict__)
print()

print('6.')
class EnvLet:
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to
susan = EnvLet('Susan', 'Dave')
dave = EnvLet('Dave', 'Susan')
print(susan.__dict__)
print(dave.__dict__)