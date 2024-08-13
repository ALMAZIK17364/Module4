class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        if new_floor > 0 and new_floor <= self.numbers_of_floors:
            a = 1
            while a <= new_floor:
                print(a)
                a += 1
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numbers_of_floors}"

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        self.numbers_of_floors += value
        return self

    def __radd__(self, value):
        self.numbers_of_floors += value
        return self

    def __iadd__(self, value):
        self.numbers_of_floors += value
        return self
    #"__radd__(self, value), __iadd__(self, value) - работают так же
    # как и __add__ (возвращают результат его вызова)." - Т.е. они буквально делают одно и тоже?
    # Или скобки не обЪясняют отличия от __add__, а объясняют её функционал,
    # тогда я сделал __add__ неправильно, но я делал ровно по заданию..
    # Не уверен, верно ли я понял условия 3 и 4 пунктов задачи.
    pass




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__