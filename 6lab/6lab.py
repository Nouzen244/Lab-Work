# Задание 1: Защита данных пользователя
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

# Задание 2: Полиморфизм и наследование
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{self.make} {self.model}, топливо: {self.fuel_type}"

user = UserAccount(input("Имя: "), input("Email: "), input("Пароль: "))
print(f"Аккаунт создан: {user.username}")

new_pass = input("Новый пароль: ")
user.set_password(new_pass)
print("Пароль изменен")

check_pass = input("Проверить пароль: ")
print(f"Верность пароля: {user.check_password(check_pass)}")

car = Car("Toyota", "Camry", "бензин")
print(car.get_info())
