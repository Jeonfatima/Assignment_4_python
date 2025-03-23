"""
Program: add2numbers
--------------------
Another python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.
"""
def main():
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    result = num1 + num2
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()