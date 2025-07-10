# 2.	Пребройте броя на липсващите стойности за всяка колона в df_students.

import pandas as pd
import numpy as np

data = {'Име': ['Алиса', 'Боб', 'Чарли', 'Дейвид', 'Ева'],
        'Възраст': [25, np.nan, 22, 35, np.nan],
        'Оценка': [8.5, 9.2, np.nan, 9.5, 8.9],
        'Град': ['София', None, 'София', 'Варна', 'Бургас']}
df_students = pd.DataFrame(data)

# Преброяване на липсващите стойности за всяка колона
# Методът .isnull() връща булев DataFrame.
# Методът .sum() приложен без аргумент 'axis' (или с axis=0) сумира по колони,
# третирайки True като 1 и False като 0.
missing_count_per_column = df_students.isnull().sum()

print("Оригинален DataFrame:")
print(df_students)
print("\nБрой на липсващите стойности за всяка колона:")
print(missing_count_per_column)