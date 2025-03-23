def main():
    numbers : list = [1,2,3,4]
    doubled : list = [i * 2 for i in numbers]
    print("Initial list is : " + str(numbers))
    print("Doubled list is : " + str(doubled))

if __name__=="__main__":
    main()