import pytest
from library.book import Book
from library.library import Library

@pytest.fixture
def library():
    return Library()

@pytest.fixture
def book1():
    return Book("Antigone", "Jean Anouilh")

@pytest.fixture
def book2():
    return Book("La Boîte à merveilles", "Ahmed Sefrioui")


def test_add_book(library, book1, book2):
    library.add_book(book1)
    library.add_book(book2)
    assert len(library.books)==2

def test_remove_book(library, book1, book2):
    library.add_book(book1)
    library.add_book(book2)
    library.remove_book(book1)
    assert len(library.books)==1
    with pytest.raises(ValueError):
        library.remove_book(book1)

def test_find_book_by_title(library, book1, book2):
    library.add_book(book1)
    library.add_book(book2)
    book= library.find_book_by_title("La Boîte à merveilles")
    assert book is not None
    assert book.title== "La Boîte à merveilles"
    assert book.author == "Ahmed Sefrioui"

def test_list_books(library, book1, book2):
    library.add_book(book1)
    library.add_book(book2)
    books_List = library.list_books()
    assert "Antigone by Jean Anouilh" in books_List
    assert "La Boîte à merveilles by Ahmed Sefrioui" in books_List