# 1.	Експортиране с caption и label: Създайте DataFrame с данни за продажби (продукт, количество, цена). Експортирайте го в LaTeX, като добавите подходящ caption и label към таблицата.

import pandas as pd

# --- 1. Създаване на DataFrame с данни за продажби ---
df = pd.DataFrame({
    'Продукт': ['Книга', 'Химикал', 'Тетрадка'],
    'Количество': [15, 30, 25],
    'Цена (лв.)': [12.50, 1.20, 3.80]
})

# --- 2. Експортиране в LaTeX формат с caption и label ---
latex_code = df.to_latex(
    buf='sales_table.tex',
    index=False,                     # Без индекс в таблицата
    caption='Таблица с продажбите за седмицата',  # Заглавие (caption)
    label='tab:sales_data',         # Етикет за референции в LaTeX
    encoding='utf-8'
)

# --- 3. Запис в .tex файл ---
with open('sales_table.tex', 'w', encoding='utf-8') as f:
   df.to_latex(f, index=False, float_format='{:.2f}'.format)

# --- 4. Преглед на LaTeX кода ---
print(latex_code)

#=============================================Обяснение:=====================================================
#
# index=False изключва индекса от таблицата (не е нужен в повечето случаи за печат).
#
# caption задава заглавието на таблицата.
#
# label позволява препратки към таблицата в LaTeX с \ref{tab:sales_data}.
#
# to_latex() автоматично добавя необходимата LaTeX структура за таблици.