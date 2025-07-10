#6.	Дефинирайте два класа: Book (Книга) и Library (Библиотека).
# Клас Book:
# •	Конструктор (__init__), който приема и инициализира следните атрибути:
	# o	title (заглавие) - стринг
	# o	author (автор) - стринг
	# o	publisher (издателство) - стринг
	# o	year (година на издаване) - цяло число
	# o	isbn (ISBN номер) - стринг
# •	Дефинирайте метод __str__, който връща четим стринг, описващ информацията за книгата (например: "Заглавие: [Заглавие], Автор: [Автор], ...").
# Клас Library:
# •	Конструктор (__init__), който приема и инициализира:
	# o	name (име на библиотеката) - стринг
	# o	books (списък с книги) - празен списък по подразбиране.
# •	Дефинирайте следните методи:
	# o	add_book(book): приема обект от клас Book и го добавя към списъка books.
	# o	search_by_author(author): приема стринг author и връща списък с всички книги в библиотеката, написани от този автор.
	# o	display_book_info(isbn): приема стринг isbn и търси книга с този ISBN. Ако бъде намерена, извежда информацията за книгата, използвайки метода __str__ на обекта Book. Ако не бъде намерена, извежда подходящо съобщение.
	# o	remove_book(isbn): приема стринг isbn и премахва книгата с този ISBN от списъка books, ако съществува. Извежда подходящо съобщение за успех или неуспех.
	#Напишете примерен код, който демонстрира използването на класовете Book и Library  и техните методи, като създадете библиотека, добавите няколко книги, извършите търсене, изведете информация и премахнете книга.

# Клас за представяне на книга
class Book:
    def __init__(self, title: str, author: str, publisher: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn

    def __str__(self):
        # Връща информацията за книгата във форматиран вид
        return (f"Заглавие: {self.title}, Автор: {self.author}\n"
                f"Издателство: {self.publisher}, Година на издаване: {self.year}\n"
                f"ISBN: {self.isbn}")

# Клас за представяне на библиотека
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []  # Списък от книги

    def add_book(self, book: Book):
        # Добавя книга към библиотеката
        self.books.append(book)
        print(f"Книгата със заглавие '{book.title}' е добавена!\n")

    def search_by_author(self, author: str):
        # Търси книги от даден автор (без значение на главни/малки букви)
        result = [book for book in self.books if book.author.lower() == author.lower()]
        return result

    def display_book_info(self, isbn: str):
        # Показва информация за книга по ISBN
        for book in self.books:
            if book.isbn == isbn:
                print(book)
                print()
                return
        print(f"Книга с ISBN: {isbn} не е намерена!\n")

    def remove_book(self, isbn: str):
        # Премахва книга по ISBN
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Книгата със заглавие '{book.title}' е премахната!\n")
                return
        print(f"Книга с ISBN: {isbn} не е намерена!\n")

# Създаване на обекти от тип Book
book1 = Book("Под игото", "Иван Вазов", "Български писател", 1894, "9789540901234")
book2 = Book("Немили-недраги", "Иван Вазов", "Захарий Стоянов", 1883, "9789540905678")
book3 = Book("Бай Ганьо", "Алеко Константинов", "Христо Г. Данов", 1895, "9789540901111")
book4 = Book("Винету", "Карл Май", "Сиела", 1965, "1010101251")  # поправен тип на 'year'

# Създаване на библиотека
my_library = Library("Земеделец 1900")

# Добавяне на книги
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)

# Показване на информация за книги по ISBN
my_library.display_book_info("1010101251")
my_library.display_book_info("9789540901234")

# Търсене по автор
books_by_vazov = my_library.search_by_author("Иван Вазов")
print("Книги от Иван Вазов:")
for b in books_by_vazov:
    print("-", b.title)
print()

# Премахване на книга
my_library.remove_book("9789540905678")

# Опит за премахване на несъществуваща книга
my_library.remove_book("0000000000")




