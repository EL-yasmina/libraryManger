import pytest
from library.book import Book

def test_book_initialisation():
    book = Book("Antigone", "Jean Anouilh")
    assert book.title == "Antigone"
    assert book.author == "Jean Anouilh"


def test_book_str():
    book = Book("Antigone","Jean Anouilh")
    assert str(book) == "Antigone by Jean Anouilh"