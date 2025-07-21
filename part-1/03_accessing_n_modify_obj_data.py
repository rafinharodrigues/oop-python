class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def greet(self,personName):
        print(f"Hello {personName}, my name is {self.username}.")


user1 = User("rafarodriguesp","rafa@gmail.com","1234")
print(user1.email)
user1.greet("Daniel")

user1.email = "anything"
print(user1.email)