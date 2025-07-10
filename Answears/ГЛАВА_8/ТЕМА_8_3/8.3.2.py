# 2.	Съединете два DataFrame-а по индекс, като използвате вътрешно съединяване (inner join).

import pandas as pd

# Примерни данни за първия DataFrame
df_left = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
}, index=[1, 2, 3])  # Индексът играе ролята на 'ID'

# Примерни данни за втория DataFrame с частично съвпадащи индекси
df_right = pd.DataFrame({
    'Grade': ['A', 'A+']
}, index=[1, 2])  # Само ID 1 и 2 съвпадат

# Вътрешно съединяване по индекс
joined_inner = df_left.join(df_right, how='inner')

# Показваме резултата
print(joined_inner)


# Коментар:
# С параметъра how='inner' се запазват само тези редове, за които има съвпадащи индекси и в двата DataFrame-а.
#
# Това е еквивалентно на INNER JOIN в SQL.