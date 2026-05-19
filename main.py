import json

FILE = "books.json"

def main():
    books = load_books()

    while True:
        print("""
        1. Добавить книгу
        2. Показать все книги
        3. Показать среднюю оценку
        4. Статистика по авторам
        5. Удалить книгу
        6. Выход
        """)

        choice = input("Выбор: ")

        if choice == "1":
            add_book(books)
            save_books(books)

        elif choice == "2":
            show_books(books)

        elif choice == "3":
            print(average_rating(books))

        elif choice == "4":
            print(author_stats(books))

        elif choice == "5":
            delete_book(books)
            save_books(books)

        elif choice == "6":
            break


def load_books():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(books):
    author = input("Автор: ")
    title = input("Название: ")
    rating = int(input("Оценка (1-5): "))
    date = input("Дата прочтения: ")

    # проверка дубликатов
    for b in books:
        if b["author"] == author and b["title"] == title:
            print("Книга уже существует!")
            return

    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })