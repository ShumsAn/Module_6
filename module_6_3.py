
class Horse:

    def __init__(self):
        self.sound = 'Frrr'
        self.x_distance = 0
        super().__init__()

    def run(self, dx):
        """где dx - изменение дистанции, увеличивает x_distance на dx."""
        self.dx = dx
        self.x_distance = self.x_distance + dx
class Eagle :

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__()
    def fly(self, dy):
        """где dy - изменение дистанции, увеличивает y_distance на dy."""
        self.dy = dy
        self.y_distance = self.y_distance + dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()


    def move(self, dx, dy):
        """где dx и dy изменения дистанции.
        В этом методе должны запускаться наследованные методы run и fly соответственно"""
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        """возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке."""
        return  (self.x_distance,self.y_distance)

    def voice (self):
        """ печатает значение унаследованного атрибута sound"""

        print(f'{self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
