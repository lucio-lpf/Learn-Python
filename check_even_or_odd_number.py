from problem_solver import ProblemSolver

def is_number(test_param):
        try:
            int(test_param)
        except ValueError:
            return False;
        else:
            return True



problem_object = ProblemSolver()

number = raw_input("Choose a number: ")
division_number = raw_input("Choose another number to divide the last one: ")
if is_number(number) and is_number(division_number):
    problem_object.check_even_or_odd_number(int(number),int(division_number))
else:

    print("You need to inform a integer number, pls")























