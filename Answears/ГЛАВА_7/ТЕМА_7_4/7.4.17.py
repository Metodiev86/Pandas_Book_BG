#17.	Даден е DataFrame с колони 'old_name_1' и 'old_name_2'. Напишете код, който ги преименува на 'new_name_1' и 'new_name_2' съответно, използвайки .rename().

import pandas as pd

# Примерен DataFrame с колони 'old_name_1' и 'old_name_2'
df = pd.DataFrame({
    'old_name_1': [1, 2, 3],
    'old_name_2': [4, 5, 6]
})

# Използваме .rename() за да преименуваме колоните
df = df.rename(columns={'old_name_1': 'new_name_1', 'old_name_2': 'new_name_2'})

print(df)
