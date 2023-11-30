class User:
    def __init__(self):
        self.__name = "Неизвестно"
        self.__surname = "Неизвестно"
        self.__email = "Неизвестно"
        self.__password = "Неизвестно"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password
