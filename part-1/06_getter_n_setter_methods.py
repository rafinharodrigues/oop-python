class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    def getThisUserEmail(self):
        return self._email
    
    def setThisUserEmail(self,newEmail):
        self._email = newEmail


user1 = User("rafarodriguesp","teste@email.com","123455")

print(user1.getThisUserEmail())
user1.setThisUserEmail("segundoteste@gmail.com")
print(user1.getThisUserEmail())