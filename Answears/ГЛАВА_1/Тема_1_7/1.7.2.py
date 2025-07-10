#Напишете функция, която приема низ като аргумент и връща неговата дължина.

def string_len(my_string: str) -> int:  # Дефинираме функцията с параметър my_string
    return len(my_string)  # Връщаме дължината на низа с вградената функция len()

print(string_len("Python is cool"))  # Извикваме функцията с низ и отпечатваме резултата
print(string_len("Hello"))  # Извежда 5
print(string_len("1234567890"))  # Извежда 10
print(string_len(""))  # Извежда 0
