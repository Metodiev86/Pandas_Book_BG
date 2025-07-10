#7.	Запълнете липсващите стойности в колоната 'Оценка' с предишната валидна оценка (използвайте ffill).

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

# Запълване на липсващите стойности в колоната 'Оценка' с предишната валидна стойност
# 'ffill' (forward fill) запълва NaN със стойността от предишния валиден ред.
df_students['Оценка'] = df_students['Оценка'].fillna(method='ffill')

print("\nDataFrame след запълване на липсващите стойности в 'Оценка' с 'ffill':")
print(df_students)