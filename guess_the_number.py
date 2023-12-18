import random

def main():
    secret_number = random.randint(0, 100)
    guessed = False

    print("Guess a number between 0 and 100")

    while not guessed:
        attempt = int(input("Choose a number!: "))
        if attempt == secret_number:
            print("Congratulations! You won!")
            guessed = True
        elif attempt < secret_number:
            print("More high!")
        else:
            print("Less!")

    print("Game over!")

main()