#Създайте клас Engine с метод start() и клас Car с атрибут engine (инстанция на Engine). Класът Car трябва да има метод start_engine(), който извиква метода start() на своя engine. Това е пример за композиция. Разширете примера, като добавите клас ElectricEngine с различно поведение на start(), и покажете как лесно можете да смените двигателя на колата (гъвкавост на композицията).

class Engine:
    @property
    def name(self) -> str:
        return "Двигател с вътрешно горене"

    def start(self) -> str:
        return "Двигателят е стартиран!"


class ElectricEngine:
    @property
    def name(self) -> str:
        return "Електрически двигател"

    def start(self) -> str:
        return "Стартираме електрическия двигател!"


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        print(f"Опит за стартиране на: {self.engine.name}")
        print(self.engine.start())

    def change_engine(self, new_engine):
        self.engine = new_engine
        print(f"Двигателят е сменен с: {new_engine.name}")


# Демонстрация
gas_engine = Engine()
electric_engine = ElectricEngine()

my_car = Car(gas_engine)

# Стартиране с двигател с вътрешно горене
my_car.start_engine()
print()

# Смяна с електрически двигател
my_car.change_engine(electric_engine)
my_car.start_engine()
print()

# Връщане към оригиналния двигател
my_car.change_engine(gas_engine)
my_car.start_engine()
