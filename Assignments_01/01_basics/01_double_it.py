def main():
    number = int(input("Enter a number: "))
    double = number * 2
    while double <= 100:
        print(f"{number} doubled is {double}")
        number = double
        double = double * 2
    print(f"we stop here as next double = {double}, which is greater than 100")

if __name__=="__main__":
    main()