def main():
    dividend : float = float(input("Enter the number to be divided: "))
    divisor : float = float(input("Enter the number to divide by:"))
    quotient  = dividend // divisor
    remainder  = dividend % divisor
    print("the result of this division is "+ str(quotient)+ " with a remainder of "+str(remainder))

if __name__=="__main__":
    main()