def main():
    lst = []
    value = input("Enter a value:")
    while value:
        lst.append(value)
        value = input("Enter a value or press enter to stop :")
    print("The list is : "+str(lst))

if __name__=="__main__":
    main()