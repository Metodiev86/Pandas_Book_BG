#37.	Даден е категориален Series с размери ('S', 'M', 'L'). Напишете код, който добавя категория 'XL'.

import pandas as pd

# Създаване на категориален Series
sizes = pd.Series(pd.Categorical(['S', 'M', 'L', 'M', 'S'], categories=['S', 'M', 'L'], ordered=False))

# Добавяне на нова категория 'XL'
sizes = sizes.cat.add_categories('XL')

print(sizes)
print("\nКатегории след добавяне:", sizes.cat.categories)
