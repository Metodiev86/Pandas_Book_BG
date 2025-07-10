#1.	Дадени са два DataFrame-а с еднакви колони ('Име', 'Възраст'). Напишете код, който ги комбинира по редове в нов DataFrame.

import pandas as pd

# Примерни DataFrame-и с еднакви колони
df1 = pd.DataFrame({
    'Име': ['Алиса', 'Боб'],
    'Възраст': [25, 30]
})

df2 = pd.DataFrame({
    'Име': ['Чарли', 'Дейвид'],
    'Възраст': [22, 28]
})

# Комбиниране по редове чрез pd.concat()
df_combined = pd.concat([df1, df2], ignore_index=True)

print(df_combined)
