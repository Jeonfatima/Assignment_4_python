import random
def main():
    secret_number = random.randint(1,99)

    guess = int(input("Enter a number between 1-99 to guess : "))
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is  high")
        elif guess < secret_number :
            print("Your guess is low")

        guess = int(input("Enter your guess again : "))

    print(f"Congratulations! You guessed the right number => {secret_number}")
        

if __name__=="__main__":
    main()