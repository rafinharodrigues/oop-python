class Player():
    def __init__(self,name,surname,age,user_id,identifiers=False):
        self.name = name
        self.surname = surname
        self.age = age
        self.user_id = user_id
        self.identifiers = identifiers

    def speak(self):
        print("O Player:",self.name,"está falando.")

    def getPlayerAge(self):
        print("A idade do Player",self.name,"é",self.age)


player1 = Player("Djeimes","Nego",26,2283)
player2 = Player("Indio","Cacique",30,5582)

player1.speak()
player1.getPlayerAge()
player2.speak()
player2.getPlayerAge()