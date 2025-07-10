# 4.	Работа с множество обекти: Създайте два различни DataFrame-а и една Series. Запишете ги в един HDF5 файл под различни ключове. След това прочетете обратно всеки от обектите, използвайки техните ключове.

import pandas as pd
import numpy as np

# --- 1. Създаване на два DataFrame и една Series ---
df_клиенти = pd.DataFrame({
    'Име': ['Анна', 'Боби'],
    'Град': ['София', 'Пловдив']
})

df_поръчки = pd.DataFrame({
    'Номер': [101, 102],
    'Сума': [250.5, 180.0]
})

серия_години = pd.Series([1990, 1985, 2000], name='Година на раждане')

# --- 2. Записване във файл с различни ключове ---
with pd.HDFStore('multi_objects.h5', mode='w') as store:
    store.put('клиенти', df_клиенти)
    store.put('поръчки', df_поръчки)
    store.put('години', серия_години)

print("Обектите са записани успешно в multi_objects.h5.")

# --- 3. Прочитане по ключове ---
with pd.HDFStore('multi_objects.h5', mode='r') as store:
    df_read_clients = store['клиенти']
    df_read_orders = store['поръчки']
    series_read_years = store['години']

# --- 4. Принтиране на резултатите ---
print("\n--- Клиенти ---")
print(df_read_clients)

print("\n--- Поръчки ---")
print(df_read_orders)

print("\n--- Години ---")
print(series_read_years)
