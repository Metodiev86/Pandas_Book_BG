import pandas as pd
import numpy as np
import os

# --- 1. Път до файла за кеш ---
cache_file = 'cached_data.pkl'

# --- 2. Функция за симулиране на извличане на данни с кеширане ---
def get_data_with_cache(file_path=cache_file):
    if os.path.exists(file_path):
        # Ако файлът съществува – зареждаме данните от кеш
        print("Зареждаме данните от кеширан pickle файл...")
        data = pd.read_pickle(file_path)
    else:
        # Ако файлът не съществува – генерираме нови данни
        print("Генерираме нови данни и ги кешираме...")
        data = pd.DataFrame({
            'ID': np.arange(1, 11),
            'Стойност': np.random.rand(10) * 100
        })
        data.to_pickle(file_path)
    return data

# --- 3. Извикване на функцията и преглед на резултата ---
result = get_data_with_cache()
print("\nДанни:")
print(result)
