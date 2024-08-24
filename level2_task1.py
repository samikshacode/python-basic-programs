import random
no_to_guess=random.randint(1,100)
attempts=0
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100")
while True:
    user_guess=int(input("Enter your guess:"))

    attempts+=1
    if user_guess==no_to_guess:
        print(f"Congratulations!You guessed the number in{attempts}attempts.")
        break
    elif user_guess<no_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")        
