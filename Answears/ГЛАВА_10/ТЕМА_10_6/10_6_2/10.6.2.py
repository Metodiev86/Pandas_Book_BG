# 2.	Работа с вложен JSON: Създайте JSON файл nested_data.json със следната структура:
# 	{
#   "users": [
#     {"id": 1, "info": {"name": "Alice", "age": 25}},
#     {"id": 2, "info": {"name": "Bob", "age": 30}}
#   ]
# }
# Прочетете го в DataFrame, като използвате pd.json_normalize(), за да "сплескате" вложената структура. Изведете DataFrame-а.

import pandas as pd
import json

# --- 1. Създаване на вложен JSON и запис във файл ---
nested_data = {
    "users": [
        {"id": 1, "info": {"name": "Alice", "age": 25}},
        {"id": 2, "info": {"name": "Bob", "age": 30}}
    ]
}

with open("nested_data.json", "w", encoding="utf-8") as f:
    json.dump(nested_data, f, ensure_ascii=False, indent=2)

# --- 2. Зареждане на JSON от файл ---
with open("nested_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- 3. Използване на pd.json_normalize() за сплескване на вложените структури ---
df = pd.json_normalize(data["users"])
print("Сплескан DataFrame от вложен JSON:\n")
print(df)

#============================================ Резултат: ========================================
#
# DataFrame с колони:
#
# id – идентификатор на потребителя
#
# info.name – името на потребителя
#
# info.age – възраст на потребителя