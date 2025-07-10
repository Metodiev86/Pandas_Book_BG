#3.	Запис на няколко DataFrame-а: Създайте два DataFrame-а с произволни данни. Запишете ги в един Excel файл multiple_sheets.xlsx на два отделни листа, съответно "Обобщени данни" и "Детайли". Не включвайте индексите при записването.

import pandas as pd

# --- 1. Създаване на два DataFrame-а с произволни данни ---

# Първият DataFrame – "Обобщени данни"
df_summary = pd.DataFrame({
    'Категория': ['A', 'B', 'C'],
    'Продажби': [1500, 2300, 1800],
    'Бройки': [100, 140, 120]
})

# Вторият DataFrame – "Детайли"
df_details = pd.DataFrame({
    'Продукт': ['Продукт 1', 'Продукт 2', 'Продукт 3', 'Продукт 4'],
    'Категория': ['A', 'B', 'A', 'C'],
    'Цена': [15.5, 23.0, 14.8, 19.5],
    'Количество': [50, 70, 50, 60]
})

# --- 2. Записване в един Excel файл с два листа ---

output_file = 'multiple_sheets.xlsx'

# Използваме ExcelWriter с контекстен мениджър, за да пишем в няколко листа
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_summary.to_excel(writer, sheet_name='Обобщени данни', index=False)
    df_details.to_excel(writer, sheet_name='Детайли', index=False)

# --- 3. Потвърждение ---
print(f"Двата DataFrame-а са успешно записани в '{output_file}' в отделни листове.")
