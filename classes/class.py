import random

class Calculation:
    def __init__(self, n) -> list:
        self.nums = [random.randint(1, 100) for _ in range(n)]

    def sum(self):
        return sum(self.nums)

    def mean(self):
        return sum(self.nums) / len(self.nums)

    def min_max(self):
        return min(self.nums), max(self.nums)
    
class Book:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author
    
# book = Book("Zaregoto", "Nisio Isin")

# print(book.name)
# print(book.author)
