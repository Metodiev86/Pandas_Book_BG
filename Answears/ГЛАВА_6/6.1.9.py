#9.	Създайте нов DataFrame, който съдържа само редовете от df_students, където броят на не-липсващите стойности е поне 3.

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

# Създаване на нов DataFrame с редове, които имат поне 3 не-липсващи стойности
# Параметърът 'thresh' указва минималния брой не-липсващи стойности, които редът/колоната трябва да има, за да не бъде премахнат.
df_students_at_least_3_valid = df_students.dropna(thresh=3)

print("\nDataFrame с редове, имащи поне 3 не-липсващи стойности:")
print(df_students_at_least_3_valid)