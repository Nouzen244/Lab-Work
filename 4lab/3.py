# Задание 1: функции для разных типов чтения файла
filename1 = 'example.txt'
def read_example_file(mode=' '):
    with open(filename1, 'r', encoding='utf-8') as file:
        if mode == 'all':
            content = file.read()
            print(content)
        elif mode == 'lines':
            lines = file.readlines()
            for number, line in enumerate(lines, start=1):
                print(f"{number}: {line.rstrip()}")
        else:
            print("Укажите режим: 'all' или 'lines'")
read_example_file('all')    # Чтение всего файла сразу
read_example_file('lines')  # Построчное чтение

# Задание 2: запись текста user в новый файл
def write_new_f(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return f'данные записаны в файл({filename})'
filename = input('Введи название файла: ')
content = input("Что добавить:")
result = write_new_f(filename, content)
print(result)


# Если добавить запись
filename2 = 'user_input.txt'
content = input("Введите текст для добавления в файл(Добавится на следующей строке, старый текст сохраниться. Если ничего не хотите добавлять, то просто пропустите, нажав ENTER): ")
def append_text(filename2, content):
    with open(filename2, 'a', encoding='utf-8') as file:
        file.write('\n' + content)
        return f'Данные добавлены в файл: {filename2}'
res1 = append_text(filename2, content)
print(res1)

# Задание 3: обработка FileNotFoundError

def read_example_file_safe(mode=' '):
    try:
        with open('example.txt', 'r', encoding='utf-8') as file:
            if mode == 'all':
                content = file.read()
                print(content)
            elif mode == 'lines':
                lines = file.readlines()
                for number, line in enumerate(lines, start=1):
                    print(f"{number}: {line.rstrip()}")
            else:
                print("Укажите режим: 'all' или 'lines'")
    except FileNotFoundError:
        print(" Ошибка: файл 'example.txt' не найден. Проверьте, что он существует.")

read_example_file_safe('all')
read_example_file_safe('lines')
