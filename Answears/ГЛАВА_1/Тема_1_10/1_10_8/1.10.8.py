#Създайте програма, която чете CSV файл (Comma Separated Values) и извежда данните в табличен вид на конзолата. Можете да използвате вградения модул csv на Python.

import csv  # Импортираме модула csv, който предоставя функционалности за работа с CSV файлове.

def print_csv_as_table(filename):
    try:
        # Опитваме се да отворим файла в режим на четене с UTF-8 кодировка.
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)  # Създаваме обект 'reader', който ще чете редове от CSV файла.
            rows = list(reader)  # Прочитаме всички редове в списък.

            # Проверка дали CSV файлът е празен.
            if not rows:
                print("Файлът е празен.")
                return

            # Изчисляваме максималната ширина за всяка колона, за да можем да форматираме добре таблицата.
            # zip(*rows) събира всички елементи от една и съща колона заедно.
            # max(len(str(cell)) for cell in col) намира максималната дължина на елемент в колона.
            col_widths = [max(len(str(cell)) for cell in col) for col in zip(*rows)]

            # Отпечатваме заглавията и данните по редове, като се уверяваме, че всяка колона е изравнена по ширина.
            for row in rows:
                # Форматираме реда, като използваме ljust(), за да изравним всяка клетка по ширина на съответната колона.
                formatted_row = " | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths))
                print(formatted_row)  # Отпечатваме форматирания ред.

    except FileNotFoundError:
        # Ако файлът не бъде намерен, отпечатваме съобщение за грешка.
        print(f"Файлът '{filename}' не съществува.")
    except Exception as e:
        # Ако възникне друга грешка, я отпечатваме.
        print(f"Възникна грешка: {e}")

# Пример за извикване на функцията с името на CSV файл, който ще се изведе в табличен вид.
print_csv_as_table("my_csv_file.csv")
