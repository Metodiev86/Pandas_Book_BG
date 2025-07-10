#Напишете функция, която приема име на текстов файл и премахва всички празни редове от него, като записва промените обратно в същия файл.

def remove_empty_lines(filename):
  # Отваряме файла за четене в режим 'r' и използваме utf-8 за кодировка
  with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # Четем всички редове от файла в списък

  # Използваме list comprehension, за да премахнем празните редове
  # Методът strip() премахва всички водещи и завършващи интервали и нови редове
  non_empty_lines = [line for line in lines if line.strip() != '']

  # Отваряме същия файл за запис в режим 'w', което ще презапише съдържанието на файла
  with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(non_empty_lines)  # Записваме обратно редовете без празни

  print(f"Празните редове от '{filename}' са премахнати.")  # Потвърдително съобщение
