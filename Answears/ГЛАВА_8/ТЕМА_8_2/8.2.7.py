# 7.	Слейте два DataFrame-а, които имат колони с еднакви имена (но не са ключовете за сливане), и използвайте параметъра suffixes за да ги разграничите.

import pandas as pd

# Създаваме първия DataFrame – данни от източник 1
df_source1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Anna', 'Boris'],
    'Score': [85, 90]
})

# Създаваме втория DataFrame – данни от източник 2 (същите колони, различни стойности)
df_source2 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Anna', 'Boris'],
    'Score': [88, 92]
})

# Сливане по 'ID', като разграничаваме дублиращите се колони чрез параметъра suffixes
merged_df = pd.merge(df_source1, df_source2, on='ID', suffixes=('_src1', '_src2'))

# Показваме резултата
print(merged_df)


# Коментари:
# Използваме suffixes=('_src1', '_src2'), за да избегнем конфликти между колоните 'Name' и 'Score', които съществуват и в двата DataFrame-а.
#
# Създаденият резултат съдържа колони 'Name_src1', 'Name_src2', 'Score_src1', 'Score_src2'.