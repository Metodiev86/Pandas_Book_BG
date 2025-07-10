#	Създайте клас Student (студент) с атрибути name (име) и grades (списък с оценки). Добавете метод average_grade(), който изчислява и връща средната оценка на студента. Създайте обект Student, добавете няколко оценки и изведете средната оценка.

# Създаваме клас Student (студент)
class Student:
    def __init__(self, name: str, grades: list[float]):
        """
        Конструктор на класа Student.
        :param name: Името на студента
        :param grades: Списък с оценки (float)
        """
        self.name = name
        self.grades = grades

    def average_grade(self) -> float:
        """
        Метод за изчисляване на средната оценка на студента.
        :return: Средна оценка (float)
        """
        if not self.grades:
            return 0.0  # Защита от делене на 0, ако няма оценки
        return sum(self.grades) / len(self.grades)


# Създаваме обект от класа Student с име и списък от оценки
student = Student("Стоян", [4, 4, 6, 5, 6, 6])

# Извеждаме името на студента
print(f"Име на студента: {student.name}")

# Извеждаме списъка с оценки
print(f"Оценки: {student.grades}")

# Извеждаме средната оценка, форматирана с 2 знака след десетичната запетая
print(f"Средна оценка: {student.average_grade():.2f}")
