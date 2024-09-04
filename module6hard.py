from math import pi,sqrt

class Figure:
    """Родитель Где  __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)"""
    sides_count = 0
    def __init__(self,color,*sides):
        if type(self) == Cube and len(sides) == 1:
            self.__sides = list(sides) * 12

        elif type(self) == Cube and  len(sides) != self.sides_count:
            self.__sides = [1 for num in range(self.sides_count)]

        elif len(sides) != self.sides_count:
            self.__sides = [1 for num in range(self.sides_count)]

        else:
            self.__sides = list(sides)
        self. __color = list(color)
        self.filled = True

    def get_color(self):
        """возвращает список RGB цветов"""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
         перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 """
       return (0<=r<=255 and 0<=g<=255 and 0<=b<=255)


    def set_color(self,r, g, b):
        """ изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность"""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self,*args):
        """принимает неограниченное кол-во сторон, возвращает True
        если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
         False - во всех остальных случаях."""
        self.valid_s = False
        if len(args) == len(self.__sides):
            for sides_a in args:
                if isinstance(sides_a, int) and sides_a > 0:
                    self.valid_s = True
                else:
                    self.valid_s = False
                    break
        return self.valid_s

    def get_sides(self):
        """ возвращает значение атрибута __sides"""
        return self.__sides

    def  __len__(self):
        """возвращает периметр фигуры"""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """ должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
        в противном случае - менять."""
        if self.sides_count == len(new_sides):
            self.__is_valid_sides(*new_sides)
            if self.valid_s:
                self.__sides = list(new_sides)
        return self.__sides

class Circle(Figure):

    def __init__(self,color,*sides):
        self.sides_count = 1
        super().__init__(color,*sides)
        self.__radius = self.__len__() / (2 * pi)

    def get_r(self):
        """Радиус окружности"""
        return self.__radius

    def get_square(self):
        """Площадь окружности"""
        return (self.__radius**2) * pi

class Triangle(Figure):
    def __init__(self,color,*sides):
        self.sides_count = 3
        super().__init__(color,*sides)

    def get_square(self):
        """Расчет площади треугольника по Фо́рмуле Герона
        где p - полупериметр треугольника a,b,c - длины его сторон"""

        p = 0.5 * self.__len__()
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        square = sqrt(p * (p - a) * (p - b) * (p - c))
        return square

class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12
        super().__init__(color,*sides)

    def get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

#Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

#Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# f1 = Triangle((255,5,6),10,20,22)
# f2 = Circle((213,4,5),3)
# f3 = Cube((12,4,255),10,12,10,10,12,10,10,12,10,10,12)
#
# print(f'Стороны треугольника = {f1.get_sides()}')
# print(f'Цвет треугольника {f1.get_color()}')
# f1.set_color(1,255,81)
# print(f'Цвет  треугольника после смены :{f1.get_color()}')
# # print(f'Радус = {f1.get_radius()}')
# print(f'Площадь  треугольника = {f1.get_square()}')
# # print(f1.get_square())
# print(f'Площадь круга {f2.get_square()}')
# print(f'Радиус круга {f2.get_r()}')
#
# print(f'Cтороны куба {f3.get_sides()}')
# print(f'Обьем куба {f3.get_volume()}')


