# 5.	Персонализиран индекс: Създайте DataFrame с данни за трима студенти (име, факултетен номер, среден успех). Използвайте факултетните номера като индекс на DataFrame-а. Изведете индекса на DataFrame-а.

import pandas as pd

# Данни за студентите: [фак. номер, дисциплина, успех]
students_data = [
    [123, 'Бел', 3.52],
    [224, 'Анг', 5.47],
    [333, 'Гео', 3.42]
]

# Извличане на факултетните номера (индекси)
faculty_numbers = [student[0] for student in students_data]

# Създаване на DataFrame без колоната "No", защото тя вече ще бъде индекс
df = pd.DataFrame(
    [student[1:] for student in students_data],  # премахваме фак. номер от редовете
    index=faculty_numbers,
    columns=["Дисциплина", "Среден успех"]
)

# Извеждане на индекса на DataFrame-а
print("DataFrame с факултетни номера като индекс:\n")
print(df)

print("\nИндекс на DataFrame-а:")
print(df.index)
