# qa_python

collected 18 items                                                                                                                                                    

1. Проверка добавления новой книги в словарь books_genre и проверка ключа и значания, равному ""
tests.py::TestBooksCollector::test_add_new_book_one_name_add_one_book PASSED                                                                                    [  5%]
2. Проверка, что книга находится в books_genre  и жанр находятся в списке genre 
tests.py::TestBooksCollector::test_set_book_genre_check_name_and_genre PASSED                                                                                   [ 11%]
3. Проверка присвоение книги жанра, через проверку значания в первой позиции словаря
tests.py::TestBooksCollector::test_set_book_genre_exist_name_set_genre PASSED                                                                                   [ 16%]
4.Проверка получения жанра книги, переданной в словарь book_genre 
tests.py::TestBooksCollector::test_get_book_genre_exist_name_get_genre PASSED                                                                                   [ 22%]
5. Проверка добавления названия книги_1 в списке books_with_specific_genre 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_exist_genre_get_books[\u0425\u043e\u0431\u0431\u0438\u0442-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 27%]
6.Проверка добавления названия книги_2 в списке books_with_specific_genre 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_exist_genre_get_books[\u0428\u0435\u0440\u043b\u043e\u043a \u0425\u043e\u043b\u043c\u0441-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 33%]
7. Проверка добавления названия книги_4 в списке books_with_specific_genre 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_exist_genre_get_books[\u0411\u0443\u0440\u0430\u0442\u0438\u043d\u043e-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 38%]
8. Проверка получения списка book_genre при вызове функции
tests.py::TestBooksCollector::test_get_books_genre_get_books_list PASSED                                                                                        [ 44%]
9. Проверка добавления книги в список книг для детей books_for_children, если ее жанр не находится в списке genre_age_rating и проверка, что книга, жанр которой находится в списке genre_age_rating не попадает в список books_for_children
tests.py::TestBooksCollector::test_get_books_for_children_get_children_books PASSED                                                                             [ 50%]
10. Проверка, что книга_1, которую хотят добавить находится в списке books_genre и что после добавления книги, она попадает в список favorites 
tests.py::TestBooksCollector::test_add_book_in_favorites_exist_name_add_in_favorites[\u0425\u043e\u0431\u0431\u0438\u0442-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 55%]
11.  Проверка, что книга_2, которую хотят добавить находится в списке books_genre и что после добавления книги, она попадает в список favorites 
tests.py::TestBooksCollector::test_add_book_in_favorites_exist_name_add_in_favorites[\u0428\u0435\u0440\u043b\u043e\u043a \u0425\u043e\u043b\u043c\u0441-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 61%]
12.  Проверка, что книга_3, которую хотят добавить находится в списке books_genre и что после добавления книги, она попадает в список favorites 
tests.py::TestBooksCollector::test_add_book_in_favorites_exist_name_add_in_favorites[\u0411\u0443\u0440\u0430\u0442\u0438\u043d\u043e-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 66%]
13. Добавление книги_1 в список favorites. Провека, что книга выбранная для удаления из списка favorites, больше не в списке. 
tests.py::TestBooksCollector::test_delete_book_from_favorites_exist_name_delete_book[\u0425\u043e\u0431\u0431\u0438\u0442-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 72%]
14. Добавление книги_2 в список favorites. Провека, что книга выбранная для удаления из списка favorites, больше не в списке. 
tests.py::TestBooksCollector::test_delete_book_from_favorites_exist_name_delete_book[\u0428\u0435\u0440\u043b\u043e\u043a \u0425\u043e\u043b\u043c\u0441-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 77%]
15. Добавление книги_3 в список favorites. Провека, что книга выбранная для удаления из списка favorites, больше не в списке. 
tests.py::TestBooksCollector::test_delete_book_from_favorites_exist_name_delete_book[\u0411\u0443\u0440\u0430\u0442\u0438\u043d\u043e-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 83%]
16.Проверка добавления книги_1 в список favorites  и получение списка favorites.
tests.py::TestBooksCollector::test_get_list_of_favorites_books_get_favorites_books[\u0425\u043e\u0431\u0431\u0438\u0442-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 88%]
17.Проверка добавления книги_2 в список favorites  и получение списка favorites.
tests.py::TestBooksCollector::test_get_list_of_favorites_books_get_favorites_books[\u0428\u0435\u0440\u043b\u043e\u043a \u0425\u043e\u043b\u043c\u0441-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 94%]
18.Проверка добавления книги_3 в список favorites  и получение списка favorites.
tests.py::TestBooksCollector::test_get_list_of_favorites_books_get_favorites_books[\u0411\u0443\u0440\u0430\u0442\u0438\u043d\u043e-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [100%]

