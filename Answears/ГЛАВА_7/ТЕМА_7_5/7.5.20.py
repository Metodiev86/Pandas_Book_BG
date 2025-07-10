# 20.	Даден е DataFrame с колона 'ID'. Напишете код, който задава тази колона като индекс на DataFrame-а, използвайки .set_index().

import pandas as pd

# Примерен DataFrame с колона 'ID'
df = pd.DataFrame({
    'ID': [101, 102, 103],
    'Име': ['Анна', 'Боби', 'Чарли'],
    'Град': ['София', 'Пловдив', 'Варна']
})

# Задаваме колоната 'ID' като нов индекс на DataFrame-а
df = df.set_index('ID')

print(df)
