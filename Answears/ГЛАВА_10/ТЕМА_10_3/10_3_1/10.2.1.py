# 1.	Запазване и зареждане на DataFrame: Създайте DataFrame с произволни данни. Запазете го в pickle файл с име my_data.pkl. След това прочетете pickle файла обратно в нов DataFrame и изведете съдържанието му, за да се уверите, че данните са запазени и възстановени правилно.

import pandas as pd
import numpy as np
from sqlalchemy.sql.traversals import compare

# --- 1. Създаване на DataFrame с произволни данни ---
# Създаваме данни за 5 служителя
data = {
    'Име': ['Анна', 'Борис', 'Виктор', 'Галя', 'Даниел'],
    'Възраст': np.random.randint(25, 50, 5),
    'Град': ['София', 'Пловдив', 'Варна', 'Бургас', 'Русе'],
    'Заплата': np.random.randint(3000, 7000, 5)
}
df_original = pd.DataFrame(data)

# Преглеждаме оригиналния DataFrame
print("Оригинален DataFrame:\n")
print(df_original)

# --- 2. Запазване на DataFrame като pickle файл ---
pickle_path = 'my_data.pkl'  # Име на файла
df_original.to_pickle(pickle_path)
print(f"\nDataFrame-ът е запазен като pickle файл: {pickle_path}")

# --- 3. Зареждане на pickle файла в нов DataFrame ---
df_loaded = pd.read_pickle(pickle_path)

# Преглеждаме заредения DataFrame
print("\nЗареден DataFrame от pickle файла:\n")
print(df_loaded)
print()

print(f"Данните от oригиналния DataFrame и заредените данни от pickle файла еднакви ли са: {df_original.equals(df_loaded)}")