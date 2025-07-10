# 3.	Експортиране с десетична запетая: Създайте DataFrame с числа с плаваща запетая. Експортирайте го в LaTeX, като използвате запетая като десетичен разделител.

import pandas as pd

# --- 1. Създаване на DataFrame с float стойности ---
df = pd.DataFrame({
    'Продукт': ['A', 'B', 'C'],
    'Цена (лв)': [12.5, 8.75, 100.33],
    'Отстъпка (%)': [5.25, 10.0, 0.0]
})

# --- 2. Експортиране в LaTeX с десетична запетая ---
latex_code = df.to_latex(
    index=False,
    decimal=',',       # ТУК се използва запетая като десетичен разделител
    caption='Таблица с цени и отстъпки',
    label='tab:decimal_comma',
    escape=False
)

# --- 3. Запис във файл ---
with open('decimal_comma_table.tex', 'w', encoding='utf-8') as f:
    f.write(latex_code)

print("LaTeX файлът 'decimal_comma_table.tex' е записан успешно.")
