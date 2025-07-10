#1.	Идентифицирайте всички липсващи стойности в df_students и изведете булев DataFrame.

import pandas as pd
import numpy as np

data = {'Име': ['Алиса', 'Боб', 'Чарли', 'Дейвид', 'Ева'],
        'Възраст': [25, np.nan, 22, 35, np.nan],
        'Оценка': [8.5, 9.2, np.nan, 9.5, 8.9],
        'Град': ['София', None, 'София', 'Варна', 'Бургас']}
df_students = pd.DataFrame(data)

# Идентифициране на всички липсващи стойности
# Методът .isnull() връща булев DataFrame със същата форма като оригиналния,
# където True указва липсваща стойност, а False - налична.
missing_values_df = df_students.isnull()

print("Оригинален DataFrame:")
print(df_students)
print("\nБулев DataFrame, показващ липсващите стойности:")
print(missing_values_df)