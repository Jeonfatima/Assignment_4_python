def main():
    print("Welcome to Madlib Game!")
    print("------------------------")
    print("Enter the following to generate a story.\n")
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb1 = input("First Verb: ")
    verb2 = input("Second verb:")
    place = input("Enter a place: ")
    madlib = f"On a {adjective} afternoon, a {noun} suddenly decided to {verb1} in the middle of the {place}, surprising everyone who was {verb2}. It was a moment no one would ever forget."
    print(f"Here's your generated story \n {madlib}")

if __name__=="__main__":
    main()