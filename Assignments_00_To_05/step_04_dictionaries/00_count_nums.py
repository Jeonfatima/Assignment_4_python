def user_input():
    user_numbers = []
    while True:
        number = input("Enter a number (or press Enter to stop): ")  # Read as string
        if number == "":  # Stop when user presses Enter
            break
        user_numbers.append(int(number))  # Convert to int only if input is not empty
    return user_numbers  # Return the list

def count_num(num_list):
    num_dict = {}
    for number in num_list:
        if number not in num_dict:
            num_dict[number] = 1
        else:
            num_dict[number] += 1
        
    return num_dict

def print_number(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times")
    
def main():
    input_numbers = user_input()
    final_num = count_num(input_numbers)
    print(input_numbers)
    print_number(final_num)

if __name__=="__main__":
    main()