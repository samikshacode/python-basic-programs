import random
def number_guesser():
    print("Welcome to the Number Guesser!")

    lower_bound=int(input("Enter the lower bound of the range:"))
    upper_bound=int(input("Enter the upper bound of the range:"))

    number_to_guess=random.randint(lower_bound,upper_bound)
    attempts=0

    while True:
        user_guess=int(input("Enter your guess:"))

        attempts+=1

        if user_guess<number_to_guess:
            print("Too low!Try again.")

        elif user_guess>number_to_guess:
            print("Too High! Try again")
       
        else:
            print(f"Congratulation You;ve guessed the number {number_to_guess} correctly in {attempts} attempts.")

            
number_guesser()