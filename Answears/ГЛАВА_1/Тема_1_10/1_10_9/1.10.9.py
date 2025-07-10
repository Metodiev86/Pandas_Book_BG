#Напишете код, който чете голям текстов файл (който може да не се побере в паметта) и преброява честотата на всяка дума в него. Резултатът трябва да бъде записан в друг файл, сортиран по честота (от най-честата към най-рядката).

def clean_word(word):
    """Премахва пунктуация от дума и я прави малка"""
    cleaned = ""  # Създаваме празен низ за почистената дума.
    for char in word:
        if char.isalnum():  # Ако символът е буква или цифра, го добавяме към почистената дума.
            cleaned += char
    return cleaned.lower()  # Връщаме думата в малки букви, за да се избегнат проблеми със сравнението.

def count_word_frequency(input_file_path: str, output_file_path: str):
    word_freq = {}  # Речник, който ще съхранява честотата на всяка дума.

    with open(input_file_path, 'r', encoding='utf-8') as file:
        # Четем файла ред по ред. Това е полезно за големи файлове, които не могат да се поберат в паметта.
        for line in file:
            words = line.strip().split()  # Разделяме реда на отделни думи.
            for word in words:
                word = clean_word(word)  # Почистваме всяка дума.
                if word:  # Ако думата не е празна.
                    if word in word_freq:
                        word_freq[word] += 1  # Увеличаваме броя на срещанията на думата.
                    else:
                        word_freq[word] = 1  # Записваме думата за първи път и задаваме начална стойност 1.

    # Сортиране на думите по стойността им (честотата), в низходящ ред (най-честите първи).
    sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

    # Отваряме изходния файл за запис.
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for word, count in sorted_words:
            out_file.write(f"{word}: {count}\n")  # Записваме всяка дума и нейната честота в изходния файл.

# Примерно извикване на функцията:
count_word_frequency("text.txt", "result.txt")

