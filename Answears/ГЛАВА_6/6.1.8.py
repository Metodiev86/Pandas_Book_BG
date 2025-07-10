# 8.	Интерполирайте липсващите стойности в колоната 'Възраст', използвайки линейна интерполация.

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

# Интерполиране на липсващите стойности в колоната 'Възраст'
# Методът .interpolate() по подразбиране използва 'linear' интерполация.
df_students['Възраст'] = df_students['Възраст'].interpolate(method='linear')

print("\nDataFrame след интерполиране на липсващите стойности във 'Възраст':")
print(df_students)