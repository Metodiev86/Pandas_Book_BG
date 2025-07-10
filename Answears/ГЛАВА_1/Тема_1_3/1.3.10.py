#Напишете код, който приема число (цяло или десетично) и го преобразува към булева стойност. Експериментирайте с
# различни числа (включително 0 и отрицателни) и обяснете резултатите.

# Дадени числа
zero = 0
positive_number = 5
negative_number = -10

# Преобразуване на числата в булеви стойности
bool_zero = bool(zero)               # 0 се преобразува в False
bool_positive_number = bool(positive_number)  # Положително число се преобразува в True
bool_negative_number = bool(negative_number)  # Отрицателно число се преобразува в True

# Извеждаме резултатите
print(f"bool_zero = {bool_zero}")                      # False
print(f"bool_positive_number = {bool_positive_number}")  # True
print(f"bool_negative_number = {bool_negative_number}")  # True

