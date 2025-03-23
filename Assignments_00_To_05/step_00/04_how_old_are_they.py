"""
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen."""

def main():
    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew : int = chen + anton
    ethan : int = chen

    print(f"Anton is {anton} years old")
    print("Beth is "+str(beth)+ " years old")
    print(f"Chen is {chen} years old")
    print(f"Drew is {drew} years old")
    print(f"Ethan is {ethan} years old")


if __name__ == "__main__":
    main()