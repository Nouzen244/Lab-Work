from package import timebase

result = timebase.get_form_timeint()
print("Текущая дата и время:", result)


from package import mathematic

try:
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
except ValueError:
    print("Ошибка: пожалуйста, введи число ^^")

result_plus = mathematic.plus(a, b)
result_minus = mathematic.minus(a, b)
result_umnoj = mathematic.umnoj(a, b)
if b == 0:
    result_deli = "Ошибка: деление на ноль :c"
else:
    result_deli = mathematic.deli(a, b)
print("\n-------------")
print(f"{a} + {b} = {result_plus}\n{a} - {b} = {result_minus}\n{a} / {b} = {result_deli}\n{a} * {b} = {result_umnoj}")