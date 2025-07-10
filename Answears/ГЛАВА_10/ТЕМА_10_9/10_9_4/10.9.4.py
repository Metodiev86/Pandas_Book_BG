# 4.	Експортиране с MultiIndex колони: Създайте DataFrame с MultiIndex колони (например, нива 'Статистика' и поднива 'Средно', 'Стандартно отклонение'). Експортирайте го в LaTeX и наблюдавайте как се представя структурата. Опитайте да използвате escape=False за по-лесно четене на кода.

import pandas as pd
import numpy as np

# --- 1. Създаване на MultiIndex за колоните ---
columns = pd.MultiIndex.from_product(
    [['Статистика'], ['Средно', 'Стандартно отклонение']]
)

# --- 2. Създаване на примерни данни ---
data = np.array([
    [23.5, 4.2],
    [31.8, 3.6],
    [29.0, 5.1]
])

df = pd.DataFrame(data, columns=columns, index=['Група A', 'Група B', 'Група C'])

# --- 3. Експортиране в LaTeX ---
latex_code = df.to_latex(
    multicolumn=True,
    multicolumn_format='c',
    escape=False,
    caption='Описателна статистика по групи',
    label='tab:multiindex_stats'
)

# --- 4. Запис във файл ---
with open('multiindex_table.tex', 'w', encoding='utf-8') as f:
    f.write(latex_code)

print("Файлът 'multiindex_table.tex' е записан успешно.")



#=============================================Забележка:=====================================================
#
# multicolumn=True и multicolumn_format='c' са задължителни, за да видиш групираните заглавия в LaTeX.
#
# escape=False позволява използване на символи като %, без те да се ескейпват автоматично.
#
# Ако искаш по-добро форматиране (например подравняване или локално изчисляване), можем да добавим и .style.