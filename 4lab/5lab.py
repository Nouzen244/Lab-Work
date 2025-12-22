import math
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, автор: {self.author}, год издания: {self.year}"

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

title = input("Название: ")
author = input("Автор: ")
year = input("Год издания: ")
book = Book(title, author, year)
print(book.get_info())


def c_and_mo_circle():
    radius = float(input("Радиус: "))
    circle = Circle(radius)
    initial_radius = circle.get_radius()
    new_radius = float(input("Введи новый радиус: "))
    circle.set_radius(new_radius)
    final_radius = circle.get_radius()
    return initial_radius, final_radius

# book_info = c_and_s_book()
initial_radius, final_radius = c_and_mo_circle()

def results():
    print("------------")
    print(book_info)
    print(f"Исходный радиус!: {initial_radius}")
    print(f"Новый радиус!: {final_radius}")

results()
