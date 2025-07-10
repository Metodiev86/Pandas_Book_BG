# 5.	Запис с включен индекс като атрибут: Създайте DataFrame с произволен индекс (не поредица от числа) и една колона с данни. Запишете го в XML файл indexed_output.xml, като включите индекса като атрибут на елемента за ред.

import pandas as pd

# Създаване на DataFrame с индекс
data = pd.DataFrame({
    'Стойност': [100, 200, 300]
}, index=['ID_A', 'ID_B', 'ID_C'])

# Преместваме индекса като обикновена колона
data_reset = data.reset_index()
data_reset.rename(columns={'index': 'id'}, inplace=True)

# Записваме като XML, указвайки колоната 'id' като атрибут
data_reset.to_xml(
    'indexed_output.xml',
    root_name='данни',
    row_name='запис',
    index=False,
    attr_cols=['id']
)

print("Файлът 'indexed_output1.xml' беше записан успешно.")

