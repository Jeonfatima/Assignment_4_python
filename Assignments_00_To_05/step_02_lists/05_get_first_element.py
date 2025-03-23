def get_first_element(lst):
    print("The first element is " + lst[0])

def main():
    lst = []
    element : str = input("Enter the element of the list: ")
    while element != "":
        lst.append(element)
        element = input("Enter the element of the list or press an enter to stop: ")
    
    get_first_element(lst)

if __name__=="__main__":
    main()