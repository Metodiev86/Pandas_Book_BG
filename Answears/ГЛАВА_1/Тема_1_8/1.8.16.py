#Създайте клас DataProcessor, който има вътрешен (защитен) списък _data. Предоставете публичен метод add_data(item) за добавяне на елементи към списъка и @property за достъп до дължината на списъка (data_length). Опитайте да промените директно _data отвън и обсъдете резултата.

class DataProcessor:
    def __init__(self):
        self.__data = []  # частен атрибут с name mangling

    def add_data(self, item):
        """Добавя елемент към списъка."""
        self.__data.append(item)

    def remove_data(self, item):
        """Премахва елемент, ако съществува."""
        if item in self.__data:
            self.__data.remove(item)
        else:
            print(f"Елементът {item} не съществува.")

    def clear_data(self):
        """Изчиства всички елементи."""
        self.__data.clear()

    def get_data(self):
        """Връща КОПИЕ на списъка – не може да се променя директно!"""
        return self.__data.copy()

    @property
    def data_length(self):
        """Връща дължината на списъка."""
        return len(self.__data)

dp = DataProcessor()

dp.add_data(10)
dp.add_data(20)

print("Брой елементи:", dp.data_length)       # -> 2
print("Съдържание:", dp.get_data())           # -> [10, 20]

dp.remove_data(10)
print("След премахване:", dp.get_data())      # -> [20]

# Опит за директен достъп (няма да работи)
try:
    print(dp.__data)  # Грешка: атрибутът не съществува
except AttributeError as e:
    print("ГРЕШКА при достъп:", e)

# Директният достъп всъщност е скрит под друго име
print("Ниско ниво достъп (не се препоръчва):", dp._DataProcessor__data)  # Възможно, но неофициално!
