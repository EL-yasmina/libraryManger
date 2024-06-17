import pytest
from library.book import Book
from library.library import Library

@pytest.fixture
def library():
    return Library()

def test_library_integration(library):
    # Ajouter des livres
    book1 = Book("Antigone", "Jean Anouilh")
    book2 = Book("La Boîte à merveilles", "Ahmed Sefrioui")
    library.add_book(book1)
    library.add_book(book2)
    assert len(library.books) == 2

    # Rechercher un livre par titre
    found_book = library.find_book_by_title("La Boîte à merveilles")
    assert found_book is not None
    assert found_book.title == "La Boîte à merveilles"
    assert found_book.author == "Ahmed Sefrioui"

    # Vérifier la liste des livres
    books_list = library.list_books()
    assert "Antigone by Jean Anouilh" in books_list
    assert "La Boîte à merveilles by Ahmed Sefrioui" in books_list

    # Supprimer un livre
    library.remove_book(book1)
    assert len(library.books) == 1
    assert library.find_book_by_title("Antigone") is None

    # Essayer de supprimer un livre non existant (doit lever une exception)
    with pytest.raises(ValueError):
        library.remove_book(book1)
