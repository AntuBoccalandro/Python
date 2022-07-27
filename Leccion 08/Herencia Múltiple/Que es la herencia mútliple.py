# Es el proceso en el cuál podemos dar las propiedades y métodos de varias clases padres a una clase hija. Por ejemplo:

class User:
    def __init__(self, name):
        self.name = name

class User_pro:
    def __init__(self, name, username):
        super().__init__(self, name, username)
        self.username = username