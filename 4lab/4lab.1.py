import datetime
import my_module
ch = input("Введите ваши 2 числа через пробел: ")
a, b = map(int, ch.split())
res = my_module.plus(a, b)
print('Сумма = ', res)

res1 = my_module.minus(a, b)
print('Вычит. = ', res1)

res2 = my_module.deli(a, b)
print('Деление = ', res2)

res3 = my_module.umnoj(a, b)
print('Произв. = ', res3)

now_time = datetime.datetime.now()
print(f'текущая дата и время {now_time}')