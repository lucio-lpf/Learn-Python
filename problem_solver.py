from person import Person
import random

class ProblemSolver():   


    def year_one_hundred(self,name,age,number_of_copies):
        tom = Person(name,int(age))
        for i in range(number_of_copies):
            print(tom.name + ", you will become 100 yo in: " + str(tom.year_of_one_hundred()))

    def check_even_or_odd_number(self,number,division_number):

        if  number % 4 == 0:
            print("This number can be divided by 4")
        elif number % 2 == 0:
            print("You informed a even number")
        else:
            print( "You informed a odd number")

        if number % division_number == 0:
            print ("The number you informed can be divided by the division number you also informed")

    def print_less_than_number_in_list(self, my_list,last_than):
        new_list = []
        for element in my_list:
            if element < last_than:
                new_list.append(element)
        print new_list

    def creat_random_list(self):
        new_list = []
        for i in range(0, random.randint(1,10)):
            new_list.append(random.randint(1,20))
        print(new_list)
        return new_list

    def print_common_in_two_lists(self):
        list_one = self.creat_random_list()
        list_two = self.creat_random_list()
        common_list = list(set(list_one) & set(list_two))     
        print common_list

    def is_number(self, test_param):
        try:
            int(test_param)
        except ValueError:
            return False;
        else:
            return True

    def guess_game(self,guess,random_number,count_guesses):
        
            count_guesses += 1
            if self.is_number(guess):
                if int(guess) == random_number:
                    print("Congrats, your got it right. Let's try a new one.")
                    print("You took " +  str(count_guesses) + " to got it right")
                    count_guesses = 0
                    random_number = random.randint(1,10)
                elif int(guess) < random_number:
                    print("OPS, a little bit higher.")
                else:
                    print("OPS, a little bit lower")
            elif guess == "bye":
                 print("BYE BYE")
            else:
                print("Dont ruin my game")
            return (count_guesses, random_number)

