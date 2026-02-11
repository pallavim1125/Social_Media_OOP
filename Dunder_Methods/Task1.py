class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'"{self.title}" by {self.author} costs ₹{self.price}'

    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", {self.price})'


b1 = Book("Python Basics", "John Doe", 499)
b2 = Book("AI Guide", "Jane Smith", 799)

print(b1)        # calls __str__
print([b1, b2])  # calls __repr__
