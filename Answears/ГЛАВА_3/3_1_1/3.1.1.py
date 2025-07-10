# 1.	Зареждане и първоначален преглед:
# o	Заредете CSV файл с данни (можете да използвате произволен публичен dataset или да създадете свой собствен примерен файл).
# o	Използвайте .head() и .tail() за да разгледате първите и последните няколко реда.
# o	Използвайте .info() за да получите обща информация за DataFrame-а.

import pandas as pd

data_csv = pd.read_csv("currency.csv")

print(f"Първите пет реда са:\n {data_csv.head()}\n")
print(f"Първите 3 реда са:\n {data_csv.head(3)}\n")
print(f"Последните 5 реда са:\n {data_csv.tail(5)}\n")
print(f"Последните 3 реда са:\n {data_csv.tail(3)}\n")
print(f"{data_csv.info()}\n")