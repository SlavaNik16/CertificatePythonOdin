from Data.file_handling import *
class Management:
    def register(self):
        print("Регистрация пользователя: ")
        name = str(input("Введите ваше имя: "))
        surname = str(input("Введите вашу фамилию: "))
        email = str(input("Введите ваш адрес электронной почты: "))
        password = str(input("Введите пароль: "))

        data = read_data_from_file()
        emails = [user['email'] for user in data]
        if email in emails:
            print("Пользователь с таким электронным адресом электронной почты уже существует!")
            return
        user = {
            "name": name.strip(),
            "surname": surname.strip(),
            "email": email.strip(),
            "password": password.strip()
        }
        data.append(user)
        write_data_to_file(data)
        print("Регистрация успешно завершена!")
    def login(self):
        email = input("Введите ваш адрес электронной почты: ")
        password = input("Введите пароль: ")

        data = read_data_from_file()
        for user in data:
            if user["email"] == email and user["password"] == password:
                return user, data
        return None, None
    def update(self):
        user, data = self.login()
        if user == None:
            print("Неправильный адрес электронной почты или пароль!")
            return

        user["name"] = str(input("Введите новое имя: ")).strip()
        user["surname"] = str(input("Введите новую фамилию: ")).strip()
        user["email"] = str(input("Введите новый адрес электронной почты: ")).strip()
        user["password"] = str(input("Введите новый пароль: ")).strip()

        write_data_to_file(data)
        print("Данные успешно обновлены.")
    def delete(self):
        user, data = self.login()
        if user == None:
            print("Неправильный адрес электронной почты или пароль!")
            return
        data.remove(user)
        write_data_to_file(data)
        print("Данные успешно удалены.")


