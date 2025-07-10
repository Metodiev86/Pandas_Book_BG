# 4.	Разглеждане на атрибути: Създайте прост DataFrame с няколко колони от различен тип данни (например int, float, string). Изведете типа на данните за всяка колона, както и общия брой на елементи в DataFrame-а.


import pandas as pd  # Импортиране на библиотеката pandas

# Данни за трима студенти: факултетен номер (int), дисциплина (str), среден успех (float)
data = [
    [1, 'Bel', 3.52],
    [2, 'Ang', 5.47],
    [3, 'GEO', 3.42]
]

# Индекси – персонализирани имена на редовете
indexes = ['Student_1', 'Student_2', 'Student_3']

# Имена на колоните
columns_name = ["No", "Disciplin", "Ratting"]

# Създаване на DataFrame
df = pd.DataFrame(data, index=indexes, columns=columns_name)

# Отпечатване на DataFrame-а
print("Съдържание на DataFrame-а:\n")
print(df)

# Отпечатване на типа данни по колони
print("\nТипове на данните по колони:\n")
print(df.dtypes)

# Извеждане на общия брой елементи (редове × колони)
print(f"\nОбщ брой елементи в DataFrame-а: {df.size}")
