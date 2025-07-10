# 4.	Запазване на DataFrame с различни типове данни: Създайте DataFrame, който съдържа различни типове данни (числа, низове, дати). Запазете го в pickle файл и след това го заредете обратно. Проверете типовете на данните в заредения DataFrame, за да се уверите, че са запазени правилно.

import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. Създаване на DataFrame с различни типове данни ---
df_original = pd.DataFrame({
    'Число': [10, 20, 30],
    'Текст': ['първи', 'втори', 'трети'],
    'Дата': pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03']),
    'Булев': [True, False, True],
    'Случайно': np.random.rand(3)
})

# Преглед на оригиналния DataFrame
print("Оригинален DataFrame:")
print(df_original)
print("\nТипове данни:")
print(df_original.dtypes)

# --- 2. Запазване във файл като pickle ---
pickle_path = 'mixed_types.pkl'
df_original.to_pickle(pickle_path)

# --- 3. Зареждане обратно от pickle ---
df_loaded = pd.read_pickle(pickle_path)

# --- 4. Преглед на заредените данни и типовете ---
print("\nЗареден DataFrame от pickle:")
print(df_loaded)
print("\nТипове данни след зареждане:")
print(df_loaded.dtypes)
