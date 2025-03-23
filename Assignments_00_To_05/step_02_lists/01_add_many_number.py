"""Write a function that takes a list of numbers and returns the sum of those numbers."""

def add_numbers(num_list):
    total = 0
    for number in num_list:
        total += number
    return total
def main():
    num_list : list = [1,2,3,4,5]
    sum = add_numbers(num_list)
    print("The List of numbers is: " + str(num_list))
    print("Their sum is: " + str(sum))

if __name__=="__main__":
    main()