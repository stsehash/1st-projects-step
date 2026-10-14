import random

max_attempts = 10

random_number = random.randint(1, 100)

def guess_number():
    print("Welcome to number guessing!")
    print("A random number will be generated")
    print("Rules:")
    print("You will win immediately if the guess matches the random!")
    print("You have only 10 times to try B-)")
    print("Ready? Let's start!")

def main(number, attempts=1):
    if attempts > max_attempts:
        print("GG!")
        print("The correct answer is: ", number)
        return 
    
    guess = input(f"Attempts: {attempts}. Please enter: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid number! Please enter again.")
        return main(number, attempts)

    if guess < 1 or guess > 100: 
        print("Invalid number! Please enter again.")
        return main(number, attempts)

    if guess == random_number:
        print("OMG You win! By guessing in", attempts, "times.")
        return
    elif guess > random_number:
        print("Too High!")
        print("Try it again.")
        return main(number, attempts+1)
    else: 
        print("Too Low!")
        print("Try it again.")
        return main(number, attempts+1)

guess_number()
main(random_number)