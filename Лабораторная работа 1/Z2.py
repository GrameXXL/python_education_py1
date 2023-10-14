# TODO Найдите количество книг, которое можно разместить на дискете
size_discrete_mb = 1.44
n_page = 100  # Кол-во страниц
n_string = 50  # Кол-во строк
n_symbol_string = 25  # Кол-во символов в строке
n_symbol_all = n_page * n_string * n_symbol_string  # Общее число символов
size_book = n_symbol_all * 4 / 1024 / 1024  # Размер 1 книги в Мб
n_books = round(size_discrete_mb / size_book)  # Кол-во книг на 1 дискрете
print("Количество книг, помещающихся на дискету:", n_books)
