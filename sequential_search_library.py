def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()
    
    if title1[0] == title2[0]:
        return True
    
    return False

def sequential_search(books, book_title):
    for book in books:
        if is_similar(book['title'], book_title):
            return book['shelf']
        
    return "Buku Tidak Ditemukan"

books = [
    {'title': 'anak anak', 'shelf': 'A1'},
    {'title': 'Data structures And Algorithms', 'shelf': 'B2'},
    {'title': 'Introduction to Machine Learning', 'shelf': 'C3'},
    {'title': 'Database Management Systems', 'shelf': 'D4'}
]

book_title = input("Masukkan Judul Buku yang ingin dicari: ")
shelf_location = sequential_search(books, book_title)
print(shelf_location)
