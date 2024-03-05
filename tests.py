import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_one_name_add_one_book(self):
        collector = BooksCollector()
        name = 'Хоббит'

        collector.add_new_book(name)

        assert collector.get_book_genre(name) == ''

    def test_set_book_genre_exist_name_set_genre(self):
        collector = BooksCollector()
        name = 'Хоббит'
        genre = 'Фантастика'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

#так как выше я уже проверяю, работу функции get_book_genre
#добавил дополнительную проверку, что при вводе несуществующего имени, функция ничего возвращает.
    def test_get_book_genre_fake_name_get_genre(self):
        collector = BooksCollector()
        fake_name = 'Буратино'

        assert collector.get_book_genre(fake_name) == None


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

        assert name in collector.get_books_with_specific_genre(genre)

    def test_get_books_genre_get_books_list(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == collector.books_genre

#проверяю, что детская книга попала в список books_for_children
    def test_get_books_for_children_get_children_books(self):
        collector = BooksCollector()
        children_book = 'Буратино'
        genre = 'Мультфильмы'

        collector.add_new_book(children_book)
        collector.set_book_genre(children_book, genre)

        assert children_book in collector.get_books_for_children()

# проверяю, что взрослая книга не попала в список books_for_children
    def test_get_books_for_children_adult_book_not_in_children_books(self):
        collector = BooksCollector()
        adult_book = 'Шерлок Холмс'
        genre = 'Детективы'
        collector.add_new_book(adult_book)
        collector.set_book_genre(adult_book, genre)

        assert adult_book not in collector.get_books_for_children()

#так как функция принимает на входе тольок name и то, что проврку добавления жанар к имения я уже проверял выше
#проверил функция только с именем в списке book_ganre
    @pytest.mark.parametrize(
        'name', ['Хоббит','Шерлок Холмс','Буратино']
    )
    def test_add_book_in_favorites_exist_name_add_in_favorites(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert  name in collector.favorites

    @pytest.mark.parametrize(
        'name', ['Хоббит','Шерлок Холмс','Буратино']
    )
    def test_delete_book_from_favorites_exist_name_delete_book(self, name):
        collector = BooksCollector()
        remove_name = 'Шерлок Холмс'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(remove_name)

        assert remove_name not in collector.favorites

    @pytest.mark.parametrize(
        'name', ['Хоббит', 'Шерлок Холмс', 'Буратино']
    )
    def test_get_list_of_favorites_books_get_favorites_books(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == collector.favorites











