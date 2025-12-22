#Для удобства D:\Лабы\ВВИТ\4lab\project\package\timebase.py
from datetime import datetime
def format_now(type="Короткая"):
    now = datetime.now()
    if type == "Короткая":
        return now.strftime("%d.%m.%Y")
    elif type == "Длинная":
        return now.strftime("%d.%m.%Y года, %H:%M")
    else:
        return str(now)

def get_form_timeint():
    print("Выбери формат даты: \n1 — Короткий (XX(День).XX(Месяц).XXXX(Год)) \n2 — Длинный (xx Месяц xxxx года, чч:мм)")
    choice = input("Ваш выбор (1 или 2): ").strip()

    if choice == "1":
        return format_now("Короткая")
    elif choice == "2":
        return format_now("Длинная")
    else:
        print("Используй либо 1, либо 2. т.к. ты написал что-то другое, будет использован короткий формат.")
        return format_now("Короткая")