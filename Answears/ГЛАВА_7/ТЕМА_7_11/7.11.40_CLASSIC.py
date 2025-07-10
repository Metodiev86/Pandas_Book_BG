#40.	Даден е DataFrame. Използвайте .pipe() за да приложите последователно две функции: първата, която филтрира редовете, където стойността в колона 'А' е по-голяма от 10, и втората, която преименува колона 'Б' на 'Ново име'.

import pandas as pd

# Примерен DataFrame
df = pd.DataFrame({
    'А': [5, 15, 25],
    'Б': [100, 200, 300]
})

# Функция за филтриране
def filter_a_gt_10(df):
    return df[df['А'] > 10]

# Функция за преименуване на колона
def rename_column_b(df):
    return df.rename(columns={'Б': 'Ново име'})

# Прилагане на функциите с .pipe()
result = (
    df
    .pipe(filter_a_gt_10)
    .pipe(rename_column_b)
)

print(result)
