# 1.	Четене на JSON с различна ориентация: Създайте JSON файл data_records.json със следните данни (ориентация 'records'):
# {"name": "Alice", "age": 25}
# {"name": "Bob", "age": 30}
# {"name": "Charlie", "age": 22}
# Прочетете го в DataFrame. След това създайте друг JSON файл data_index.json със същите данни, но с ориентация 'index' (като имената са индекси). Прочетете и този файл в DataFrame. Сравнете резултатите.

import pandas as pd
import json

# --- 1. Създаване и запис на JSON файл с ориентация "records" ---
records_data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

# Записваме всеки запис на отделен ред (линия) – ориентация 'records'
with open("data_records.json", "w", encoding="utf-8") as f:
    for record in records_data:
        f.write(json.dumps(record) + "\n")

# --- 2. Четене на JSON с ориентация "records" ---
df_records = pd.read_json("data_records.json", lines=True)
print("DataFrame от JSON (records ориентация):\n")
print(df_records)

# --- 3. Създаване и запис на JSON с ориентация "index" ---
# използваме имената като индекси
index_data = {
    "Alice": {"age": 25},
    "Bob": {"age": 30},
    "Charlie": {"age": 22}
}

with open("data_index.json", "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

# --- 4. Четене на JSON с ориентация "index" ---
df_index = pd.read_json("data_index.json", orient="index")
print("\nDataFrame от JSON (index ориентация):\n")
print(df_index)

# --- 5. Сравнение ---
# При 'records': имената са стойности в колоната 'name'
# При 'index': имената стават индекс на редовете
