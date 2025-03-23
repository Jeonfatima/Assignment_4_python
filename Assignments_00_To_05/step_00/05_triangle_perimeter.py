"""Prompt the user to enter the lengths of each side of a triangle and
 then calculate and print the perimeter of the triangle (the sum of all of the side lengths)."""

def main():
    side1 : float = float(input("Enter the length of first side of triangle:"))
    side2 : float = float(input("Enter the length of second side of triangle:"))
    side3 :float = float(input("Enter the length of third side of triangle:"))
   
    print(f"The perimeter is : " + str(side1+side2+side3))

if __name__=="__main__":
    main()