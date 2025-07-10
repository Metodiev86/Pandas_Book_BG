#Напишете функция, която приема две дати като низове във формат "YYYY-MM-DD" и използва datetime.datetime.strptime() за да ги преобразува в date обекти. След това върнете разликата в дни между тях.

# Импортиране на модула datetime, който позволява работа с дати и времена
import datetime
from datetime import datetime  # Импортираме директно класа datetime за по-кратко използване

# Дефинираме функция, която приема два низа, представляващи дати във формат "YYYY-MM-DD"
def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"  # Определяме очаквания формат на датите (година-месяц-ден)

    # Преобразуваме низовете в обекти от тип date чрез datetime.strptime(),
    # след което извличаме само датата с .date()
    date1 = datetime.strptime(date_str1, date_format).date()
    date2 = datetime.strptime(date_str2, date_format).date()

    # Изчисляваме разликата между двете дати и вземаме абсолютната стойност в дни
    delta = abs((date2 - date1).days)

    return delta  # Връщаме броя дни

# Въвеждане на двете дати от потребителя
first_date_str = input("Въведете първата дата във формат YYYY-MM-DD: ")
second_date_str = input("Въведете втората дата във формат YYYY-MM-DD: ")

# Извикваме функцията и отпечатваме резултата на екрана
print(f"Разликата между {first_date_str} и {second_date_str} e {days_between_dates(first_date_str, second_date_str)} дни")
