class Animal:
    """ Родительскй класс
    Где атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
    с методом eat(self, food)  где food - это параметр, принимающий объекты классов растений"""

    alive = True
    fed = False

    def __init__(self,name):
        self.name = name

    def eat(self, food):
        self.food = (Plant)
        if food.edible == True:
            print(f'{self.name},съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False
        return self.fed, self.alive

class Mammal(Animal):
    """Наследуемый класс. Родитель -Animal"""


class Predator (Animal):
    """Наследуемый класс. Родитель -Animal"""


class Plant:
    """ Родительскй класс Растения
        Где атрибут edible = False(съедобность), name - индивидуальное название каждого растения"""

    edible = False

    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    """Наследуемый класс с атрибутом edible - сьедобность"""
    edible = True

class Flower(Plant):
    """Наследуемый класс с атрибутом edible - сьедобность"""
    edible = False


# Проверка
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)


print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
