library_inventory = {}

def add_book(isbn, title, author, genre, availability):
    
    
    
    if isbn in library_inventory:
        print(f"Book with ISBN {isbn} already exists.")
    else:
        library_inventory[isbn] = {
            'title': title,
            'author': author,
            'genre': genre,
            'availability': availability
        }
        print(f"Book '{title}' added to the library.")

def update_book_details(isbn, title=None, author=None, genre=None, availability=None):
    
    if isbn not in library_inventory:
        print(f"No book found with ISBN {isbn}.")
    else:
        if title is not None:
            library_inventory[isbn]['title'] = title
        if author is not None:
            library_inventory[isbn]['author'] = author
        if genre is not None:
            library_inventory[isbn]['genre'] = genre
        if availability is not None:
            library_inventory[isbn]['availability'] = availability
        print(f"Details for book with ISBN {isbn} updated.")

def search_by_isbn(isbn):
   
    return library_inventory.get(isbn, None)

def generate_genre_report():
    
    genre_report = {}
    for isbn, details in library_inventory.items():
        if details['availability']:
            genre = details['genre']
            if genre not in genre_report:
                genre_report[genre] = []
            genre_report[genre].append(details['title'])
    return genre_report


if __name__ == "__main__":

    add_book("978-0-1234-5678-9", "Rich poor dad", "Fiction", True)
    add_book("978-0-9876-5432-1", "atomic habbit", "Fiction", True)
    add_book("978-0-1111-2222-3","space war ", "Fiction", False)
    
    
    update_book_details("978-0-1234-5678-9", availability=False)
    
    
    book = search_by_isbn("978-0-1234-5678-9")
    if book:
        print("Book details:", book)
    else:
        print("Book not found.")
    
    
    report = generate_genre_report()
    print("Available books by genre:")
    for genre, titles in report.items():
        print(f"{genre}: {', '.join(titles)}")
