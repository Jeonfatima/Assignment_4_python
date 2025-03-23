import math
def main():
    side_AB : float = float(input("Enter the length of side AB : "))
    side_BC : float = float(input("Enter the length of side BC : "))
    side_AC : float = math.sqrt(side_AB ** 2 + side_BC ** 2)
    print(f"The length of third side (the hypoteneuse) is : {side_AC}")

if __name__ == "__main__":
    main()