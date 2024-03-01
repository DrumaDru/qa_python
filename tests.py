import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_one_name_add_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Хоббит')

        assert list(collector.books_genre.keys())[0] == 'Хоббит' and list(collector.books_genre.values())[0] == ''

    def test_set_book_genre_check_name_and_genre(self):

        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит','Фантастика')
        name = 'Хоббит'
        genre = 'Фантастика'
        assert name in collector.books_genre and genre in collector.genre

    def test_set_book_genre_exist_name_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')

        assert list(collector.books_genre.values())[0] == 'Фантастика'

    def test_get_book_genre_exist_name_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.get_book_genre('Хоббит')
        name = 'Хоббит'

        assert collector.books_genre.get(name) == 'Фантастика'


    @pytest.mark.parametrize(
        'name, genre',[
            ['Хоббит', 'Фантастика'],
            ['Шерлок Холмс','Детективы'],
            ['Буратино','Мультфильмы'],
        ]
    )
    def test_get_books_with_specific_genre_exist_genre_get_books(self, name,genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        list_books = collector.get_books_with_specific_genre(genre)
        assert  name in list_books

    def test_get_books_genre_get_books_list(self):
        collector = BooksCollector()

        collector.get_books_genre()
        assert collector.get_books_genre() == collector.books_genre


    def test_get_books_for_children_get_children_books(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Буратино')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Буратино', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        adult_book = 'Шерлок Холмс'
        children_book = 'Буратино'
        assert (children_book in children_books) and (adult_book not in children_books)

    @pytest.mark.parametrize(
        'name, genre', [
            ['Хоббит', 'Фантастика'],
            ['Шерлок Холмс', 'Детективы'],
            ['Буратино', 'Мультфильмы'],
        ]
    )
    def test_add_book_in_favorites_exist_name_add_in_favorites(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        favorites_list = collector.favorites

        assert (name in list(collector.books_genre.keys())) and (name in favorites_list)

    @pytest.mark.parametrize(
        'name, genre', [
            ['Хоббит', 'Фантастика'],
            ['Шерлок Холмс', 'Детективы'],
            ['Буратино', 'Мультфильмы'],
        ]
    )
    def test_delete_book_from_favorites_exist_name_delete_book(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        favorites_list = collector.favorites
        collector.delete_book_from_favorites('Шерлок Холмс')
        remove_name = 'Шерлок Холмс'


        assert remove_name not in favorites_list

    @pytest.mark.parametrize(
        'name, genre', [
            ['Хоббит', 'Фантастика'],
            ['Шерлок Холмс', 'Детективы'],
            ['Буратино', 'Мультфильмы'],
        ]
    )
    def test_get_list_of_favorites_books_get_favorites_books(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        favorites_list = collector.favorites

        assert collector.get_list_of_favorites_books() == favorites_list











