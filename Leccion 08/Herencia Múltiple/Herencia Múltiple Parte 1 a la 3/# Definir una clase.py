# Definir una clase
class User:
    def __init__(self, name, username):
        self.name = name
        self.username = username
    
# Creción de un objeto
user1 = User('Juan', 'Juan123')
print(user1)