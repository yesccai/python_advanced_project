class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"《{self.title}》 by {self.author}"

class Person:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        raise NotImplementedError

class Student(Person):
    def borrow_book(self, book):
        if book.available:
            book.available = False
            return f"{self.name} 借了{book}"
        else:
            return f"{book} 已被借出"

class Teacher(Person):
    def borrow_book(self, book):
        if book.available:
           book.available = False
           return f"教师 {self.name} 借阅: {book}"
        else:
            return f"{book} 已被借出"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
