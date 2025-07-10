# 3.	Дадени са два DataFrame-а, където ключът за сливане в единия е обикновена колона, а в другия е индекс. Слейте ги.

import pandas as pd

# DataFrame с ключ като колона
df_goods = pd.DataFrame({
    'Код': [101, 102, 103],
    'Име': ['Хляб', 'Мляко', 'Сирене']
})

# DataFrame с ключ като индекс
df_prices = pd.DataFrame({
    'Цена': [1.20, 2.50, 4.80]
}, index=[101, 102, 103])  # Индекс е 'Код'

# Сливане: колоната 'Код' от df_продукти съвпада с индекса на df_цени
df_result = pd.merge(df_goods, df_prices,
                       left_on='Код', right_index=True)

print(df_result)
