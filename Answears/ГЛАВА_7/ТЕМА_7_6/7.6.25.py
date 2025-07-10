#Даден е DataFrame с индекс от дати. Напишете код, който сортира DataFrame-а по дати във възходящ ред.

import pandas as pd

# Примерен DataFrame с индекс от дати в разбъркан ред
dates = pd.to_datetime(['2023-03-10', '2023-01-15', '2023-02-20'])
df = pd.DataFrame({'стойност': [100, 200, 150]}, index=dates)

# Сортиране на DataFrame-а по датите във възходящ ред
df_sorted = df.sort_index()

print(df_sorted)
