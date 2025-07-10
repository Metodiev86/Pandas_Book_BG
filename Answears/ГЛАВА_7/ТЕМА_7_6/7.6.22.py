#Даден е DataFrame с колони 'име' и 'възраст'. Напишете код, който сортира DataFrame-а по възраст в низходящ ред.

import pandas as pd

# Примерен DataFrame
df = pd.DataFrame({
    'име': ['Анна', 'Боби', 'Чарли', 'Дени'],
    'възраст': [28, 35, 22, 30]
})

# Сортиране по 'възраст' в низходящ ред
df_sorted = df.sort_values(by='възраст', ascending=False)

print(df_sorted)
