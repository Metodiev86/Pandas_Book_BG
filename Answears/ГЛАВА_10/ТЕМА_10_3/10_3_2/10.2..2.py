# 2.	Запазване на няколко обекта: Създайте два различни Pandas обекта (например, DataFrame и Series). Запазете ги в два отделни pickle файла (df.pkl и series.pkl). След това ги заредете обратно и изведете техните типове и съдържание.

import pandas as pd
import numpy as np

# --- 1. Създаване на DataFrame и Series с произволни данни ---
# Създаваме DataFrame с данни за продукти
df_products = pd.DataFrame({
    'Продукт': ['Хляб', 'Мляко', 'Сирене', 'Яйца'],
    'Цена': [1.20, 2.50, 6.30, 3.00],
    'Количество': [20, 15, 10, 30]
})

# Създаваме Series с брой продажби по месеци
monthly_sales = pd.Series(
    [120, 135, 98, 143, 110],
    index=['Януари', 'Февруари', 'Март', 'Април', 'Май'],
    name='Продажби'
)

# --- 2. Запазване на обектите в отделни pickle файлове ---
df_path = 'df.pkl'
series_path = 'series.pkl'

df_products.to_pickle(df_path)
monthly_sales.to_pickle(series_path)

print("Обектите са успешно запазени като pickle файлове.")

# --- 3. Зареждане на pickle файловете обратно ---
loaded_df = pd.read_pickle(df_path)
loaded_series = pd.read_pickle(series_path)

# --- 4. Извеждане на типовете и съдържанието ---
print("\nЗареден DataFrame:")
print(type(loaded_df))
print(loaded_df)

print("\nЗареден Series:")
print(type(loaded_series))
print(loaded_series)
