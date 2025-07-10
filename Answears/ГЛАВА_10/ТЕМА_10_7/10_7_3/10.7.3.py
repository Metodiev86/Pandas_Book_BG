# 3.	Запис в HTML с клас и без индекс: Създайте DataFrame с произволни данни. Конвертирайте го в HTML таблица, като не включвате индекса и добавите CSS клас с име "data-table" към елемента <table>. Изведете генерирания HTML код.

import pandas as pd

# Създаваме DataFrame с произволни данни
data = {
    "Име": ["Анна", "Борис", "Виктор", "Галя"],
    "Възраст": [28, 34, 45, 23],
    "Град": ["София", "Пловдив", "Варна", "Русе"]
}
df = pd.DataFrame(data)

# Конвертираме в HTML без индекс и с CSS клас "data-table"
html_table = df.to_html(index=False, classes="data-table")

# Извеждаме HTML кода
print(html_table)
