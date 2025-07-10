#Създайте клас TemperatureConverter. Той трябва да има статичен метод celsius_to_fahrenheit(celsius), който преобразува градуси по Целзий във Фаренхайт, и метод на клас from_fahrenheit(fahrenheit), който създава инстанция на класа TemperatureConverter от дадена температура по Фаренхайт (вътрешно да съхранява температурата по Целзий).

# Клас за преобразуване и представяне на температура
class TemperatureConverter:
    def __init__(self, celsius: float):
        # Инициализация със стойност в Целзий
        self.celsius = celsius

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        # Статичен метод, който преобразува Целзий във Фаренхайт
        return celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float):
        # Метод на клас, който създава обект, преобразувайки Фаренхайт в Целзий
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)  # Създава обект с изчисления Целзий

    def __str__(self):
        # Представяне на обекта като низ: показва и двете стойности
        return f"{self.celsius:.2f} °C / {self.celsius_to_fahrenheit(self.celsius):.2f} °F"

# Създаване на обект от температура в Целзий
temp1 = TemperatureConverter(25)
print(temp1)  # -> 25.00 °C / 77.00 °F

# Създаване на обект от температура във Фаренхайт
temp2 = TemperatureConverter.from_fahrenheit(77)
print(temp2)  # -> 25.00 °C / 77.00 °F
