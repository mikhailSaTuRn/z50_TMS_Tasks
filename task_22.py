print('Task 22!')
print()

print('1.')
class Tree:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def height_up(self, up):
        self.height += up

birch = Tree(640, 48)
pinetree = Tree(1024, 48)
print(birch.__dict__)
print(pinetree.__dict__)
print()
print('Changes:')
birch.height_up(2)
print(birch.height)
print()

print('2.')
class Human:
    def __init__(self, gender, age, eaten_candy):
        self.gender = gender
        self.age = age
        self.eaten_candy = eaten_candy
    def eating(self, candy):
        for i in candy:
            self.eaten_candy.append(i)
        #del self.eaten_candy[]
kate = Human('female', 30, ['mars', 'snikers', 'spartak'])
sasha = Human('male', 39, ['nuts', 'spartak'])
print(sasha.__dict__)
print(kate.__dict__)
print()
print('Changes:')
kate.eating(['nuts'])
print(kate.eaten_candy)
print()

print('3.')
class Book:
    def __init__(self, author, year, pages):
        self.author = author
        self.year = year
        self.pages = pages
    def findPage(self, numb):
        return self.pages[numb - 1]
book1 = Book('Pushkin', 1834, ['В последних', 'числах', 'сентября'])
book2 = Book('Karatkevich', 1982, ['Зорка', 'Вянера', 'узышла', 'над зямлёю'])
print(book1.__dict__)
print(book2.__dict__)
print()
print('Changes:')
print(book1.findPage(2))
print(book2.findPage(4))
print(book2.findPage(1))
print()

print('4.')
class EnvLet:
    def __init__(self, from_, to, letter):
        self.from_ = from_
        self.to = to
        self.letter = letter
    def sign(self):
        return 'С уважением, ' + self.from_
susan = EnvLet('Susan', 'Dave', 'Lorem Ipsum')
dave = EnvLet('Dave', 'Susan', 'Ipsum Lorem')
print(susan.__dict__)
print(dave.__dict__)
print()
print(susan.sign())
print()

print('5.')
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def newDate(self, days):
        self.days = days
        self.dd = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
        self.mm = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        self.day = self.day + self.days
        while self.day > self.dd[self.month]:
            self.day = self.day - self.dd[self.month]
            ind = 1
            for c in self.mm:
                if c == self.month:
                    break
                ind += 1
                if ind > 11:
                    self.year += 1
                    ind = 0
            self.month = self.mm[ind]
        return self.day, self.month, self.year
day2 = Date(18, 'November', 2020)
day5 = Date(23, 'April', 2021)
print(day2.__dict__)
print(day5.__dict__)
print()
print('Changes:')
print(day2.newDate(365)) #<--- Сюда вводить сколько прибавить дней