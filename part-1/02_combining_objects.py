class Person:
    def __init__(self,name,address,number):
        self.name = name
        self.address = address
        self.number = number

class Cat:
    def __init__(self,name,breed,age,owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def makeSound(self):
        print("O gato",self.name,"está miando.")


person1 = Person("Rafael","Rua Vicente Carlos Santiago","85 988723831")
person2 = Person("Yuri","Rua Carlos Vasconcelos","85 955236587")

cat1 = Cat("Lee","Street",11,person1)
cat2 = Cat("Junior","Street",8,person2)

print(cat1.owner.name)
cat1.makeSound()

print(cat2.owner.name)
cat2.makeSound()

