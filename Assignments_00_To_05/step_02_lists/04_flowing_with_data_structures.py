def add_three_times(my_list,data):
    for i in range(3):
        my_list.append(data)
    return

def main():
 message = input("Enter any text : ")
 my_list = []
 print("list before :" + str(my_list))
 add_three_times(my_list,message)
 print("list after :" + str(my_list))

if __name__ == '__main__':
    main()