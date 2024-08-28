class Vehicle :
    """Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели) Защищен "__"
Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно) Защищен "__"
Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками) Защищен "__"
А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания."""

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return  f"Мощность двигателя: {self.__engine_power} "

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()} \n {self.get_horsepower()} \n {self.get_color()} \n Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.upper() in str(self.__COLOR_VARIANTS).upper():
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    """Класс Sedan наследуется от класса Vehicle с собственным атрибутом
     __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)"""
    __PASSENGERS_LIMIT = 5
    


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

#Пытаемся поменять модель
vehicle1.__model = 'ЖИГА'
#Попытка поменять мощность
vehicle1.__engine_power = 100500 # Защищены от перезаписи -  "__"

# Проверяем что поменялось
vehicle1.print_info()


