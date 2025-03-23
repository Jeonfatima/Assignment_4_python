SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    print("\nHere’s your fun sentence: \n")
    print(f"\033[1m{SENTENCE_START}{adjective} {noun} {verb}!\033[0m") 

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()