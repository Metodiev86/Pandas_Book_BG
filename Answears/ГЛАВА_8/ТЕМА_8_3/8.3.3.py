# 3.	Съединете два DataFrame-а по индекс, като използвате ляво съединяване (left join) и задайте различни суфикси за колоните с еднакви имена.

import pandas as pd

# Примерни данни за левия DataFrame
df_left = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
}, index=[1, 2, 3])  # Индекс = ID

# Примерни данни за десния DataFrame с припокриваща се колона 'Score'
df_right = pd.DataFrame({
    'Score': [80, 95],
    'Grade': ['B', 'A']
}, index=[1, 2])  # Само за ID 1 и 2 има данни

# Ляво съединяване по индекс + различни суфикси
joined_left = df_left.join(df_right, how='left', lsuffix='_left', rsuffix='_right')

# Показване на резултата
print(joined_left)

# Коментар:
# how='left' указва, че запазваме всички редове от левия DataFrame.
#
# lsuffix='_left', rsuffix='_right' избягват конфликт при колона с едно и също име (Score).