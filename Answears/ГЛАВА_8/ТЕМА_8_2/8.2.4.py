#4.	Извършете ляво (left) сливане на два DataFrame-а, като запазите всички редове от левия DataFrame и добавите съответстващите от десния (ако има такива).

import pandas as pd

# Създаваме левия DataFrame с информация за ученици
df_students = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# Създаваме десния DataFrame с оценки (някои ID може да липсват)
df_grades = pd.DataFrame({
    'ID': [2, 4, 5],
    'Grade': ['B', 'A', 'C']
})

# Извършваме ляво сливане по колоната 'ID'
result = pd.merge(df_students, df_grades, on='ID', how='left')

# Резултат: всички редове от df_students + съответните оценки от df_grades (ако има такива)
print(result)

# Обяснение на параметъра how='left':
#
# Запазва всички редове от левия DataFrame (df_students).
#
# Ако има съвпадения по 'ID' в десния (df_grades), ги добавя.
#
# Когато няма съвпадение – стойността в новите колони ще бъде NaN.