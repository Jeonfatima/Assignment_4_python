def phone_book():
    """sores numbers in a phonebook"""
    phonebook = {}
    while True:
        name = input("Enter a name:")
        if name == "":
            break
        number = int(input("Enter a number : "))
        phonebook[name] = number

    return phonebook

def display_phonebook(phonebook):
    """display stored numbers"""
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """lookup numbers in phonebook"""
    while True:
        name = input("Enter a name to lookup or press enter to stop :")
        if name == "":
            break
        if name not in phonebook:
            print(str(name) + "not in phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = phone_book()
    display_phonebook(phonebook)
    lookup_numbers(phonebook)
if __name__=="__main__":
    main()

