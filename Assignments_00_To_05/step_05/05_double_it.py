def main():
    number = int(input("Enter a number: "))  # Get user input
    double = number * 2  # Double the number

    while double < 100:
        print(f"{number} doubled is {double}")
        number = double  # Update number
        double = number * 2  # Double it again

    print(f"We stop here as {double} is now 100 or greater.")

if __name__ == "__main__":
    main()
