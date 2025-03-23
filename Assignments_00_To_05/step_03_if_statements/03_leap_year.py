"""The given year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is NOT a leap year; unless:
The year is also evenly divisible by 400. Then it is a leap year."""

def main():
    year = int(input("Enter a year: "))

    if year % 4 == 0:#checks if evenly divisible by four
        if year % 100 == 0:
            if year % 400 == 0:
                print("It's a leap year!")
            else:
                print("It's not a leap year")
        else:
            print("It's a leap year")
    else:
        print("It's not a leap year")

if __name__=="__main__":
    main()