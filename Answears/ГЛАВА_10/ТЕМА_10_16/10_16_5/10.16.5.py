# 5.	(Записване с указване на dtype):
# o	Създайте Pandas DataFrame с колона 'id' (числа) и колона 'description' (текст).
# o	Свържете се с SQLite база данни.
# o	Запишете DataFrame-а в таблица items, като укажете, че колоната 'id' трябва да бъде от тип INTEGER в SQL, а 'description' от тип TEXT. Проверете типа на колоните в създадената таблица (ако е възможно с SQL команда).

import pandas as pd
import sqlite3

# Създаване на DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'description': ['Item A', 'Item B', 'Item C']
})

# Свързване към SQLite база данни (локален файл)
conn = sqlite3.connect('mydatabase.db')

# Записване на DataFrame с указване на SQL типове
df.to_sql(
    name='items',
    con=conn,
    if_exists='replace',  # презаписва ако съществува
    index=False,
    dtype={
        'id': 'INTEGER',
        'description': 'TEXT'
    }
)

# Проверка на типовете на колоните в създадената таблица
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(items)")
columns_info = cursor.fetchall()

print("Типове на колоните в таблицата 'items':")
for col in columns_info:
    col_id, name, col_type, notnull, default, pk = col
    print(f"- {name}: {col_type}")

# Затваряме връзката
conn.close()
