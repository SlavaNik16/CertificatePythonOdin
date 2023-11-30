import sys
from Management import *


def authorized_user(userAuth, data):
    while True:
        print("\nДоступные действие для авторизованных пользователей: ")
        print(
            "1) Посмотреть всех пользователей\n\t"
            "Выйти - введите любой символ\n")
        answer = input("Ваш выбор: ")
        match answer:
            case "1":
                print("Пользователи: \n")
                for user in data:
                    if userAuth["email"] in user["email"]:
                        continue
                    print(f"Фамилия имя: {user['surname']} {user['name']} \n")
            case _:
                return


def main():
    while True:
        print(
            "Выберите действие:\n\t"
            "1) Зарегистрироваться\n\t"
            "2) Войти \n\t"
            "3) Обновить учетную запись\n\t"
            "4) Удалить учетную запись\n\t"
            "Выйти - введите любой символ\n")
        answer = input("Ваш выбор: ")
        man = Management()
        print()
        match answer:
            case "1":
                man.register()
            case "2":
                user, data = man.login()
                if user == None:
                    print("Неправильный адрес электронной почты или пароль!")
                    break
                print("Авторизация успешна!")
                authorized_user(user, data)
            case "3":
                man.update()
            case "4":
                man.delete()
            case _:
                sys.exit(0)


if __name__ == '__main__':
    main()
