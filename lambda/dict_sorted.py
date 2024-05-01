# Создали список из словарей книг
asoiaf_books = [
  {'title' : 'Game of Thrones', 'published' : '1996-08-01', 'pages': 694},
  {'title' : 'Clash of Kings', 'published' : '1998-11-16', 'pages': 761},
  {'title' : 'Storm of Swords', 'published' : '2000-08-08', 'pages': 973},
  {'title' : 'Feast for Crows', 'published' : '2005-10-17', 'pages': 753},
  {'title' : 'Dance with Dragons', 'published' : '2011-07-12', 'pages': 1016}
]

# Сортируем по названию
for book in sorted(asoiaf_books, key=lambda book: book.get('title')):
  print(book)

print('-------------')

# Сортируем по датам
for book in sorted(asoiaf_books, key=lambda book: book.get('published')):
  print(book)

print('-------------')

# Сортируем по количеству страниц
for book in sorted(asoiaf_books, key=lambda book: book.get('pages')):
  print(book)