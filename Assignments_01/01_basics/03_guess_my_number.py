import random
def main():
    secret_number = random.randint(1,99)

    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is  high")
        elif guess < secret_number :
            print("Your guess is low")

        guess = int(input("Enter your guess again : "))

    print(f"Congratulations! You guessed the right number => {secret_number}")
        

if __name__=="__main__":
    main()