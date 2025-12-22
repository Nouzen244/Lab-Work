# 1.
def greet(name):
    print(f'Привет, {name}!')
greet("Alex")

# 2.
def square(number):
    print(f'Квадрат этого числа: {number**2}')
square(50)

# 3.
def max_of_two(x, y):
    print(f'Максимальное из этих чисел: {max(x, y)}')
max_of_two(50, 100)


# 1. 1. 
def greet1(name1):
    print(f'Привет, {name1}!')
username = str(input("Введите ваше имя:"))
greet1(username)

# 2.1
def square1(number1):
    print(f'Квадрат этого числа: {number1**2}')
num = int(input("Введите ваше целое число:"))
square1(num)

# 3.1
def max_of_two1(x1, y1):
    print(f'Максимальное из этих чисел: {max(x1, y1)}')
maxx1 = float(input("Введите ваше первое число:"))
maxx2 = float(input("Введите ваше второе число:"))
max_of_two1(maxx1, maxx2)
