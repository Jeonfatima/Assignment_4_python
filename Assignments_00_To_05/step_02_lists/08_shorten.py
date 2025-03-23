max_length : int = 3

def remove_element(lst):
    while len(lst) > max_length:
        last_element = lst.pop()
        print(last_element)

def main():
    lst = []
    value = input("Enter an element : ")
    while value:
        lst.append(value)
        value = input("Enter an element or press enter to stop :")
    
    print(lst)
    print("Last elements are: ")

    remove_element(lst)

if __name__=="__main__":
    main()
