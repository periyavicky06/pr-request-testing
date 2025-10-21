class Book:
    def __init__(self, title, author, status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self
