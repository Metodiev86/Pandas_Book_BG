#Напишете функция, която приема име на файл и дума като аргументи и връща броя на срещанията на тази дума в файла (без да се case-sensitive).
#	Създайте програма, която чете текстов файл и записва съдържанието му в друг файл, като преобразува всички букви в горния регистър.

def write_file_uppercase(input_file: str, output_file: str):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            content = infile.read()  # Четем цялото съдържание на файла

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(content.upper())  # Записваме преобразувания текст в главни букви
        print(f"Съдържанието е записано в {output_file} в горен регистър.")

    except FileNotFoundError:
        print(f"Файлът {input_file} не съществува.")

def count_word_occurrences(filename: str, word: str) -> int:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().lower()  # Преобразуваме съдържанието до малки букви
            word = word.lower()            # Преобразуваме и търсената дума

            # Броим срещанията
            return content.count(word)

    except FileNotFoundError:
        print(f"Файлът {filename} не съществува.")
        return 0

# Преобразуваме "in.txt" и записваме в "out.txt"
write_file_uppercase("in.txt", "out.txt")

# Броим срещания на думата "данни" в "in.txt"
count = count_word_occurrences("in.txt", "данни")
print(f"Думата 'данни' се среща {count} пъти.")
