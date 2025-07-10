#Как се работи с двоични файлове в Python? Напишете пример за четене и запис на прости двоични данни (например, списък от байтове).

def copy_image_binary(source_path, destination_path):
  # Отваряме изходния файл (source_path) в режим 'rb' (read binary) за четене на байтове.
  with open(source_path, 'rb') as src_file:
    data = src_file.read()  # Прочитаме всички байтове от изходния файл.

  # Отваряме целевия файл (destination_path) в режим 'wb' (write binary) за запис на байтове.
  with open(destination_path, 'wb') as dest_file:
    dest_file.write(data)  # Записваме прочетените байтове в новия файл.

  print(f"Картинката е копирана успешно като '{destination_path}'")  # Извеждаме съобщение за успех.


# Примерно извикване на функцията за копиране на картинка:
copy_image_binary("mini.png", "copy.png")
