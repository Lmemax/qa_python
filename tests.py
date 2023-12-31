import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert collector.get_books_rating() == {'Война и мир': 1}

    def test_set_book_rating_not_list_fails(self, collector):
        collector.set_book_rating('Подросток', 2)
        assert collector.get_book_rating('Подросток') is None

    @pytest.mark.parametrize('rate', [-1, 0, 11, 15])
    def test_set_book_rating_in_border(self, collector, rate):
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', rate)
        assert collector.get_book_rating('Война и мир') == 1

    def test_set_book_rating(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 7)
        assert collector.get_book_rating('Война и мир') == 7

    def test_get_book_rating_no_rate(self, collector):
        assert collector.get_book_rating('Подросток') is None

    def test_get_book_rating_after_add(self, collector):
        collector.add_new_book('Война и мир')
        assert collector.get_book_rating('Война и мир') == 1

    def test_get_books_with_specific_rating(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Подросток')
        collector.add_new_book('Дядя Ваня')
        collector.set_book_rating('Война и мир', 9)
        collector.set_book_rating('Подросток', 6)
        collector.set_book_rating('Дядя Ваня', 9)
        result = collector.get_books_with_specific_rating(9)
        assert (['Война и мир', 'Дядя Ваня']) == result

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == ['Война и мир']

    def test_add_book_in_favorites_not_list(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Подросток')
        assert collector.get_list_of_favorites_books() != ['Подросток']

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Дядя Ваня')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Дядя Ваня')
        assert 'Война и мир', 'Дядя Ваня' in collector.get_list_of_favorites_books
