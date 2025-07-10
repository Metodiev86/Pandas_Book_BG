#Напишете програма, която приема три числа като вход и извежда най-голямото от тях.

# Приемане на три цели числа от потребителя
first_number = int(input("Въведете първото число: "))
second_number = int(input("Въведете второто число: "))
third_number = int(input("Въведете третото число: "))

# Използване на вградената функция max() за намиране на най-голямото от трите числа
best_big_number = max(first_number, second_number, third_number)

# Извеждане на резултата във формат: най-голямото от въведените числа
print(f"Най-голямото число от {first_number}, {second_number}, {third_number} е {best_big_number}")

# Без функцията max()

# Приемане на три цели числа от потребителя
first_number = int(input("Въведете първото число: "))
second_number = int(input("Въведете второто число: "))
third_number = int(input("Въведете третото число: "))

# Предполагаме, че първото число е най-голямо
biggest = first_number

# Сравняваме второто число с текущото най-голямо
if second_number > biggest:
    biggest = second_number  # Ако второто е по-голямо, то става най-голямо

# Сравняваме третото число с текущото най-голямо
if third_number > biggest:
    biggest = third_number  # Ако третото е по-голямо, то става най-голямо

# Извеждаме най-голямото от трите числа
print(f"Най-голямото число от {first_number}, {second_number}, {third_number} е {biggest}")
