affirmation : str = "I am capable of doing anything I put my mind to."

def main():
    user_input = input("Please write the following affirmation : " + affirmation)
    if user_input != affirmation:
        print("That was not the affirmation.")
        print("Please type the following affirmation : " + affirmation)
        user_input = input()

    print("That's right! ✅")

if __name__=="__main__":
    main()