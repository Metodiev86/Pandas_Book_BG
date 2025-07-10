#4.	Напишете функция, която приема път към файл като аргумент и използва модула os.path за да върне само името на файла (без пътя и разширението).

# Импортиране на модула os, който позволява работа с файловата система
import os

# Функция, която връща името на файла без пътя и разширението
def get_filename_without_extension(filepath):
    # os.path.basename извлича само името на файла от пълния път
    # Например: "/home/user/data.txt" -> "data.txt"
    filename_with_ext = os.path.basename(filepath)

    # os.path.splitext разделя името и разширението на две части:
    # "data.txt" -> ("data", ".txt")
    # Избираме само първата част – името без разширението
    filename_without_ext = os.path.splitext(filename_with_ext)[0]

    # Връщаме крайния резултат
    return filename_without_ext

# Пример:
path = "/home/user/documents/report.pdf"
print(get_filename_without_extension(path))  # Изход: report

