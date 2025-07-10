# 13.	Проверете дали след всички операции все още има липсващи стойности в оригиналния df_students (ако сте използвали inplace=False).

import pandas as pd
import numpy as np

# ПРЕСЪЗДАВАНЕ на оригиналния DataFrame, за да сме сигурни в изходното състояние
data = {'Име': ['Алиса', 'Боб', 'Чарли', 'Дейвид', 'Ева'],
        'Възраст': [25, np.nan, 22, 35, np.nan],
        'Оценка': [8.5, 9.2, np.nan, 9.5, 8.9],
        'Град': ['София', None, 'София', 'Варна', 'Бургас']}
df_students = pd.DataFrame(data)

print("Оригинален DataFrame 'df_students' в началото:")
print(df_students)
print("-" * 30)

# Изпълняваме отново само операциите, които МОДИФИЦИРАТ df_students НА МЯСТО

# 1. Запълнете липсващите стойности в колоната 'Възраст' със средната възраст.
mean_age = df_students['Възраст'].mean()
df_students['Възраст'] = df_students['Възраст'].fillna(mean_age)
print("\nDataFrame след запълване на 'Възраст' със средната:")
print(df_students)
print("-" * 30)


# 2. Запълнете липсващите стойности в колоната 'Оценка' с предишната валидна оценка (ffill).
df_students['Оценка'] = df_students['Оценка'].fillna(method='ffill')
print("\nDataFrame след запълване на 'Оценка' с ffill:")
print(df_students)
print("-" * 30)


# 3. Интерполирайте липсващите стойности в колоната 'Възраст', използвайки линейна интерполация.
# (Тук np.nan от Ева в 'Възраст' ще бъде интерполирано ако е останало, което би трябвало да стане)
df_students['Възраст'] = df_students['Възраст'].interpolate(method='linear')
print("\nDataFrame след интерполиране на 'Възраст':")
print(df_students)
print("-" * 30)


# 4. За колоната 'Град', запълнете липсващите стойности с най-често срещания град (модата).
most_frequent_city = df_students['Град'].mode()[0]
df_students['Град'] = df_students['Град'].fillna(most_frequent_city)
print("\nDataFrame след запълване на 'Град' с модата:")
print(df_students)
print("-" * 30)

#|==========================================================================================================================|
#|=================================================== ФИНАЛНА ПРОВЕРКА =====================================================|
#|==========================================================================================================================|

print("\nФИНАЛЕН DataFrame 'df_students' след всички модифициращи операции:")
print(df_students)

final_missing_values = df_students.isnull().sum()
print("\nБрой на липсващите стойности във 'df_students' след всички операции:")
print(final_missing_values)

total_remaining_missing = final_missing_values.sum()
print(f"\nОбщ брой останали липсващи стойности: {total_remaining_missing}")