# 6.	Четене на XML с различни типове данни: Създайте XML файл mixed_data.xml:
# <items>
#   <item name="Продукт А" quantity="10" price="25.99" in_stock="true"/>
#   <item name="Продукт Б" quantity="5" price="120.50" in_stock="false"/>
# </items>
#
#  Прочетете данните в DataFrame, като се опитате да позволите на Pandas автоматично да определи типовете данни (числа, булеви стойности). Изведете DataFrame-а и проверете типовете на колоните.

import pandas as pd

# --- 1. Четене на XML файл с Pandas ---
df = pd.read_xml(
    'mixed_data.xml',       # Име на файла
    xpath='.//item'         # Извличаме всички <item> елементи
)

# --- 2. Проверка на съдържанието ---
print("DataFrame със смесени типове данни:")
print(df)

# --- 3. Проверка на типовете на колоните ---
print("\nТипове на колоните:")
print(df.dtypes)
