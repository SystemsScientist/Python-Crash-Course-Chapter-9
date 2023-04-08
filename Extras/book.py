# book.py, Chapter 9, Python Crash Course
# program executes a book class

class Book():
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def get_book(self):
        return self.title

first_book = Book('python crash course', 'programming')

print("We are using " + first_book.title.title() + " for this repository.")
print(first_book.title.title() + " is a " + first_book.genre + " text book.")



