# 3.	Премахнете редовете от df_students, които съдържат поне една липсваща стойност, и запазете резултата в нов DataFrame df_students_dropped_any.

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

# Премахване на редове, съдържащи поне една липсваща стойност
# Използваме метода .dropna() без аргумент 'axis' или с axis=0,
# което е поведението по подразбиране за премахване на редове.
# 'how='any'' е също поведение по подразбиране, което означава, че редът се премахва,
# ако има дори една липсваща стойност.
df_students_dropped_any = df_students.dropna(axis=0, how='any')

print("\nDataFrame 'df_students_dropped_any' след премахване на редове с липсващи стойности:")
print(df_students_dropped_any)