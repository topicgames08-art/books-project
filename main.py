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

def show_books(books):
    for i, b in enumerate(books):
        print(f"{i+1}. {b['author']} — {b['title']} ({b['rating']})")


def average_rating(books):
    if not books:
        return 0
    return sum(b["rating"] for b in books) / len(books)


def author_stats(books):
    stats = {}
    for b in books:
        stats[b["author"]] = stats.get(b["author"], 0) + 1
    return stats