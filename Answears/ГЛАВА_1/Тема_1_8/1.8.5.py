#5.	Дефинирайте клас Shape (фигура) с метод area(), който връща 0 (като базов случай). Създайте два подкласа Circle (окръжност) с атрибут radius и Rectangle (правоъгълник) с атрибути width и height. Предефинирайте метода area() във всеки подклас, за да изчислява съответното лице. Създайте обекти от двата подкласа и изведете техните лица.

# Базов клас Shape (Форма)
class Shape:
    def area(self) -> float:
        """Метод по подразбиране, връща 0. Предназначен за пренаписване в наследници."""
        return 0

# Клас Circle (Кръг), наследява Shape
class Circle(Shape):
    def __init__(self, radius: float):
        """Инициализация на радиуса на кръга."""
        self.radius = radius

    def area(self) -> float:
        """Изчислява и връща лицето на кръга."""
        return 3.14 * self.radius ** 2

# Клас Rectangle (Правоъгълник), наследява Shape
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        """Инициализация на ширина и височина."""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Изчислява и връща лицето на правоъгълника."""
        return self.height * self.width

# Създаваме обект от тип Circle с радиус 2
my_circle = Circle(2)
print(f"Лице на кръга: {my_circle.area():.2f}")

print()

# Създаваме обект от тип Rectangle с ширина 5 и височина 2
my_rectangle = Rectangle(5, 2)
print(f"Лице на правоъгълника: {my_rectangle.area():.2f}")

