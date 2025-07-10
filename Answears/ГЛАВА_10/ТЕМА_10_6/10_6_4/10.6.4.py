# 4.	Четене на JSON Lines: Създайте JSON Lines файл data_lines.json (всеки ред е валиден JSON обект):
# {"name": "Alice", "age": 25}
# {"name": "Bob", "age": 30}
# {"name": "Charlie", "age": 22}
#
#   Прочетете го в DataFrame, като използвате правилния параметър. Изведете DataFrame-а.

import pandas as pd

# --- 1. Създаване на JSON Lines файл ---
json_lines_content = """\
{"name": "Alice", "age": 25}
{"name": "Bob", "age": 30}
{"name": "Charlie", "age": 22}
"""

with open("data_lines.json", "w", encoding="utf-8") as f:
    f.write(json_lines_content)

# --- 2. Четене на JSON Lines файл в DataFrame ---
df = pd.read_json("data_lines.json", lines=True)

# --- 3. Извеждане на DataFrame-а ---
print("Съдържание на JSON Lines файла като DataFrame:")
print(df)

#=============================================Обяснение:=====================================================
#
# lines=True указва на read_json() да третира файла като JSON Lines, където всеки ред е отделен JSON обект.
#
# Това е подходящо за големи поточни JSON файлове, често използвани в логове или данни от API.

