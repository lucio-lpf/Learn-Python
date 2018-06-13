from person import Person
import random

class ProblemSolver():   
    
    def question_one_and_two(self):
        name = raw_input("Your name: ")
        age = input("Yout age: ") 
        number_of_copies = input("Gimme a number: ")
        tom = Person(name,age)
        for i in range(number_of_copies):
            print( tom.getAge())
            print( tom.yearsToOneHundred())

    def print_less_than_five_from_list(self, my_list,last_than):
        new_list = []
        for element in my_list:
            if element < last_than:
                new_list.append(element)
        return new_list

    def random_list_gen(self):
        new_list = []
        for i in range(0, random.randint(1,10)):
            new_list.append(random.randint(1,100))
        print(new_list)
        return new_list

    def common_in_two_lists(self):
        list_one = self.random_list_gen()
        list_two = self.random_list_gen()
        common_list = list(set(list_one) & set(list_two))     
        return common_list

    def is_number(self, test_param):
        try:
            int(test_param)
        except ValueError:
            return False;
        else:
            return True

    def my_little_guess_game(self):
        
        guess = "start"
        count_guesses = 0
        random_number = random.randint(1,10)
        while guess != "bye" :
            guess = raw_input("Guess wich number i'm hiding (1-10) or bye to quit: ")
            count_guesses += 1
            if self.is_number(guess):
                if guess == random_number:
                    print("Congrats, your got it right. Let's try a new one.")
                    print("You took " +  str(count_guesses) + " to got it right")
                    count_guesses = 0
                    random_number = random.randint(1,10)
                elif guess < random_number:
                    print("OPS, a little bit higher.")
                else:
                    print("OPS, a little bit lower")
            elif guess == "bye":
                 print("BYE BYE")
                 break
            else:
                print("Dont ruin my game")
   
solve_my_problems = ProblemSolver()
#solve_my_problems.question_one_and_two() 
#print(solve_my_problems.print(less_than_five_from_list([20,30,4,2,10,1,2,9,0,-2,3],10))
#print(solve_my_problems.common_in_two_lists())
solve_my_problems.my_little_guess_game()

