import json

FILE = "books.json"


def load_books():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def delete_book(books):
    for i, b in enumerate(books):
        print(f"{i+1}. {b['author']} — {b['title']}")

    idx = int(input("Номер книги: ")) - 1

    if 0 <= idx < len(books):
        books.pop(idx)
    else:
        print("Неверный номер")