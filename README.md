# qa_python

##Description##

Покрытие тестами приложения BooksCollector, который позволяет установить рейтинг книге и добавить ее в избранное.

###Библиотека и декараторы

Pytest - библиотека 

@pytest.fixture - декоратор на фикструру

@pytest.mark.parametrize - декаратор при параметризации


####Тесты# 

1. test_add_new_book_add_two_books - добавление двух новых книг в список

2. test_add_new_book_duplicate - проверка на то, что нельзя добавить одну и ту жк книгу дважды

3. test_set_book_rating_not_list_fails - проверка, что по книге, отсутсвующей в в списке нельзя выставить рейтинг

4. test_set_book_rating_in_border - проверка то, что рейтинг нельзя больше или меньше определенных границ (1-10)

5. test_set_book_rating - проверка выставления нового рейтинга книге, имеющейся в списке

6. test_get_book_rating_no_rate - проверка, что у недобавленной книги нет рейтинга

7. test_get_book_rating_after_add - проверка рейтинга книги после добавления в список(по умолчанию рейтинг 1)

8. test_get_books_with_specific_rating - проверка списка книг с указанным рейтингом от 1 до 10

9. test_add_book_in_favorites - проверка по добавлению книги в список избранных

10. test_add_book_in_favorites_not_list - проверка , что нельзя доавить в избранные книгу, которой нет в списке

11. test_delete_book_from_favorites - проверка удаления книги из списка избранных

12. test_get_list_of_favorites_books - проверка по наличию книг в списке избранных 

 

