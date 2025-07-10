#Създайте клас Person с атрибути name и age. Създайте подклас Employee, който наследява Person и добавя атрибут employee_id и метод get_details(), който връща информация за служителя. Създайте и клас Student, който наследява Person и добавя атрибут student_id и метод get_details(), който връща информация за студента. Демонстрирайте полиморфизъм, като създадете функция, която приема обект от тип Person и извиква неговия метод get_details() (ако съществува).

# Базов клас Person с атрибути име и години
class Person:
    def __init__(self, name, age):
        self.name = name  # Име на човека
        self.age = age    # Възраст на човека

    # Метод за връщане на базова информация – ще се замества от подкласи
    def get_details(self):
        return f"Име: {self.name}, Години: {self.age} (няма конкретна роля)"


# Клас Employee (служител), който наследява Person
class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: int):
        self.employee_id = employee_id  # ID на служителя
        super().__init__(name, age)     # Извикваме конструктора на родителския клас

    # Метод, който връща информация за служителя
    def get_details(self):
        return (f"Информация за служителя:\n"
                f"ID : {self.employee_id}\n"
                f"Име : {self.name}\n"
                f"години: {self.age}\n")


# Клас Student (студент), който също наследява Person
class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        self.student_id = student_id  # ID на студента
        super().__init__(name, age)   # Извикваме конструктора на Person

    # Метод, който връща информация за студента
    def get_details(self):
        return (f"Информация за студента:\n"
                f"ID : {self.student_id}\n"
                f"Име : {self.name}\n"
                f"години: {self.age}\n")


# Функция, която приема обект от тип Person и извиква неговия метод get_details()
# Това демонстрира полиморфизъм – различни обекти реагират по свой начин
def display_info(person: Person):
    print(person.get_details())


# Създаваме обект от тип Student
student = Student("Стела", 28, 23)

# Създаваме обект от тип Employee
employee = Employee("Стоян", 38, 26)

# Извеждаме информацията за студент и служител чрез една и съща функция
display_info(student)
print()
display_info(employee)
