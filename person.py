class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def yearsToOneHundred(self):
        yearsLast = 100 - self.age
        return str("You will become 100 yo in:" + str(yearsLast) + "years")

