# 5.	Четене на локален HTML файл: Създайте прост HTML файл (my_table.html), който съдържа една таблица с няколко реда и колони. Прочетете този файл в Pandas DataFrame, използвайки pd.read_html(). Изведете DataFrame-а.

import pandas as pd

import pandas as pd

# Отваряме файла с правилната кодировка
with open("my_table.html", "r", encoding="utf-8-sig") as f:
    tables = pd.read_html(f)

# Извеждане на броя таблици (ако има повече от една)
print(f"Брой намерени таблици: {len(tables)}")

# Прочитаме първата таблица
df = tables[0]
print("Прочетена таблица:\n", df)

