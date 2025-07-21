class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.__breed = breed

    def getThisCatName(self):
        return self.name
    
    def detThisCatBreed(self):
        return self.__breed
    

cat1 = Cat("Lee","Street")
cat2 = Cat("Louis","Bengal")

print(cat1.name)
print(cat1.detThisCatBreed())
print(cat2.name)
print(cat2.detThisCatBreed())

# Wrong way
# print(cat1.__breed)