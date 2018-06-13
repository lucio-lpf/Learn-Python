from problem_solver import ProblemSolver
import random


problem_object = ProblemSolver()

guess = "start"
random_number = random.randint(1,10)
count_guesses = 0
while guess != "bye":
    guess = raw_input("Guess wich number i'm hiding (1-10) or bye to quit: ")
    count_guesses , random_number  = problem_object.guess_game(guess,random_number,count_guesses)
    
