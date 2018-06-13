class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def year_of_one_hundred(self):
        years_left = 100 - self.age
        year = 2018 + years_left
        return year
