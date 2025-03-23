def get_last_element(lst):
    print("The last element is " + lst[len(lst)- 1])

def main():
    lst = []
    element : str = input("Enter the element of the list: ")
    while element != "":
        lst.append(element)
        element = input("Enter the element of the list or press an enter to stop: ")
    print(lst)
    get_last_element(lst)

if __name__=="__main__":
    main() 