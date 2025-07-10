#Създайте клас Person с атрибути name и age. Създайте подклас Employee, който наследява Person и добавя атрибут employee_id и метод get_details(), който връща информация за служителя. Създайте и клас Student, който наследява Person и добавя атрибут student_id и метод get_details(), който връща информация за студента. Демонстрирайте полиморфизъм, като създадете функция, която приема обект от тип Person и извиква неговия метод get_details() (ако съществува).

#Решение, чрез абстрактен клас Person:

from abc import ABC, abstractmethod

# Абстрактен клас Person, който дефинира общия интерфейс за всички типове хора
class Person(ABC):
    def __init__(self, name, age):
        self.name = name  # Име на човека
        self.age = age    # Възраст на човека

    # Абстрактен метод get_details() - всички подкласове трябва да го имплементират
    @abstractmethod
    def get_details(self):
        pass

# Подклас Employee, който наследява Person и добавя атрибут employee_id
class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: int):
        super().__init__(name, age)  # Инициализация на атрибутите от родителския клас
        self.employee_id = employee_id  # Идентификатор на служителя

    # Имплементира метода get_details() за служителя
    def get_details(self):
        return (f"Информация за служителя:\n"
                f"ID : {self.employee_id}\n"
                f"Име : {self.name}\n"
                f"Години: {self.age}")

# Подклас Student, който наследява Person и добавя атрибут student_id
class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)  # Инициализация на атрибутите от родителския клас
        self.student_id = student_id  # Идентификатор на студента

    # Имплементира метода get_details() за студента
    def get_details(self):
        return (f"Информация за студента:\n"
                f"ID : {self.student_id}\n"
                f"Име : {self.name}\n"
                f"Години: {self.age}")

# Функция, която приема обект от тип Person и извиква метода get_details()
def display_info(person: Person):
    print(person.get_details())  # Извежда информацията за дадения човек (служител или студент)

# Демонстрация:
student = Student("Стела", 28, 23)  # Създаваме обект от тип Student
employee = Employee("Стоян", 38, 26)  # Създаваме обект от тип Employee

# Извеждаме информация за студента и служителя чрез метода get_details()
display_info(student)
print()
display_info(employee)

# Следната линия би довела до грешка, защото Person е абстрактен клас и не може да се инстанцира:
# person = Person("Иван", 40)  # Ще вдигне TypeError!
