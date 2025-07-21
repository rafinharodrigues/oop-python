class Person:
    def __init__(self,name, age):
        self._name = name
        self._age = age

    def getThisPersonAge(self):
        return self._age
    

# Right access way
person1 = Person("Rafael",26)
print(person1.getThisPersonAge())


# Wrong access way
print(person1._name)