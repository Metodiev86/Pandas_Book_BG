#Напишете код, който приема десетично число като низ (например "3.14") и го преобразува към  float . Изведете
# резултата и неговия тип.

# Десетично число подадено като низ
float_string = "3.14"

# Преобразуваме низа към десетично число (тип float)
float_number = float(float_string)

# Извеждаме оригиналния низ и неговия тип
print(f'float_string = "{float_string}", тип: {type(float_string)}')

# Извеждаме преобразуваната стойност и нейния тип
print(f'float_number = {float_number}, тип: {type(float_number)}')


#Ако низът не може да се преобразува (напр. "abc"), ще получиш ValueError. За защита можеш да използваш try/except.
# try:
#     float_number = float(float_string)
# except ValueError:
#     print("Грешка: Невалиден формат за десетично число.")

