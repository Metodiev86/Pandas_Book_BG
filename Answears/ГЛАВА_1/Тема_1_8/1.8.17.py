#Дефинирайте базов клас Shape с абстрактен метод area(). Създайте два подкласа Rectangle и Circle, които наследяват Shape и имплементират метода area() за съответните фигури. Напишете функция, която приема обект от тип Shape и извежда неговата площ (демонстрирайки полиморфизъм).

from abc import ABC, abstractmethod

# Абстрактен базов клас
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Подклас за правоъгълник
class Rectangle(Shape):
    def __init__(self, height: float, width: float):  # width вместо widht
        self.height = height
        self.width = width

    def area(self) -> float:
        return self.height * self.width

# Подклас за кръг
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

# Полиморфна функция
def print_area(shape: Shape):
    print(f"Площта на фигурата е: {shape.area():.2f}")

# Демонстрация
my_rectangle = Rectangle(4, 5)
my_circle = Circle(2)

print_area(my_rectangle)  # -> 20.00
print_area(my_circle)     # -> 12.56
