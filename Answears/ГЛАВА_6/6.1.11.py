# 11.	Създайте нов DataFrame, в който липсващите стойности в числовите колони ('Възраст', 'Оценка') са запълнени със средната стойност на съответната колона, а липсващата стойност в колоната 'Град' е запълнена с 'Неизвестен'.

import pandas as pd
import numpy as np

data = {'Име': ['Алиса', 'Боб', 'Чарли', 'Дейвид', 'Ева'],
        'Възраст': [25, np.nan, 22, 35, np.nan],
        'Оценка': [8.5, 9.2, np.nan, 9.5, 8.9],
        'Град': ['София', None, 'София', 'Варна', 'Бургас']}
df_students = pd.DataFrame(data)

print("Оригинален DataFrame 'df_students':")
print(df_students)
print("-" * 30)

# Създаваме копие на DataFrame-а, за да не променяме оригинала
df_filled = df_students.copy()

# 1. Запълване на липсващите стойности в числовите колони със средната стойност
mean_age = df_filled['Възраст'].mean()
mean_grade = df_filled['Оценка'].mean()

print(f"Изчислена средна възраст: {mean_age:.2f}")
print(f"Изчислена средна оценка: {mean_grade:.2f}")

df_filled['Възраст'] = df_filled['Възраст'].fillna(mean_age)
df_filled['Оценка'] = df_filled['Оценка'].fillna(mean_grade)

# 2. Запълване на липсващите стойности в колона 'Град' с 'Неизвестен'
df_filled['Град'] = df_filled['Град'].fillna('Неизвестен')

print("\nDataFrame 'df_filled' след запълване на липсващи стойности:")
print(df_filled)