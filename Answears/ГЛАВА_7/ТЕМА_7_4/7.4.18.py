# 18.	Имате DataFrame с индекс, който няма име. Напишете код, който задава име 'ID' на индекса, използвайки .rename_axis().

import pandas as pd

# Създаваме DataFrame с безименен индекс
df = pd.DataFrame({
    'Име': ['Анна', 'Борис', 'Виктор'],
    'Възраст': [25, 30, 22]
})

# Задаваме име 'ID' на индекса с .rename_axis()
df = df.rename_axis('ID')

print(df)
