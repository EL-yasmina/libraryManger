import pytest
from library.book import Book
from library.library import Library

@pytest.fixture
def library():
    return Library()

def test_add_multiple_books_and_check_availability(library):
    # Scenario: Ajouter plusieurs livres à la bibliothèque et vérifier leur disponibilité
    
    # Ajouter plusieurs livres
    books_to_add = [
        Book("Antigone", "Jean Anouilh"),
        Book("La Boîte à merveilles", "Ahmed Sefrioui"),
        Book("L'Étranger", "Albert Camus")
    ]
    
    for book in books_to_add:
        library.add_book(book)
    
    # Vérifier que tous les livres ont été ajoutés
    assert len(library.books) == 3
    
    # Vérifier la disponibilité de chaque livre par son titre
    for book in books_to_add:
        found_book = library.find_book_by_title(book.title)
        assert found_book is not None
        assert found_book.title == book.title
        assert found_book.author == book.author
    
    # Vérifier la liste des livres
    books_list = library.list_books()
    for book in books_to_add:
        assert str(book) in books_list

def test_remove_and_check_book(library):
    # Scenario: Supprimer un livre et vérifier sa non-disponibilité
    
    # Ajouter un livre
    book = Book("Antigone", "Jean Anouilh")
    library.add_book(book)
    assert len(library.books) == 1

    # Supprimer le livre
    library.remove_book(book)
    assert len(library.books) == 0
    assert library.find_book_by_title("Antigone") is None

    # Essayer de supprimer un livre non existant (doit lever une exception)
    with pytest.raises(ValueError):
        library.remove_book(book)
