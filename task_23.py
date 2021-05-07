print('Task 23!')
print()

print('1.')
#Наследование
class Building:
    def __init__(self, floors):
        self.floors = floors

class School(Building):
    def __init__(self, color, floors):
        self.color = color
        super().__init__(floors)
    def guess(self):
        if self.color == 'red':
            print('OMG! Is it Eton College?')

class Mall(Building):
    def __init__(self, stores, floors):
        self.stores = stores
        super().__init__(floors)
    def plus_one(self):
        self.stores += 1

new_build = Building(4)
print(new_build.floors)

ssh_n13 = School('red', 2)
ssh_n13.guess()

gal_grand = Mall(100500, 6)
gal_grand.plus_one()
print(gal_grand.stores)
print()

print('2.')
#Инкапсуляция
class Factorial:
    def __smth(self, numb):
        self.total = 1
        for i in range(1, numb+1):
            self.total *= i
        return self.total
    def calculate(self, numb):
        d = self.__smth(numb)
        return d

count = Factorial()
print(count.calculate(5))
print()

print('3.')
#Полиморфизм
class Bank:
    def __init__(self, deposits):
        self.deposits = deposits
    def __add__(self, other):
        gty = self.deposits + other.deposits
        return Bank(gty)
alfabank = Bank([32, 4, 54, 65])
bsb_bank = Bank([56, 23, 11])

new_bank = alfabank + bsb_bank
print(new_bank.deposits)
