def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
   
    total_cost = 0
    for fruit in fruits:
        amount = int(input(f"Enter a amount of {fruit} you would like to buy ? "))
        price = fruits[fruit]
        total_cost += (price * amount)

    print(f"Your total is ${total_cost}")


if __name__=="__main__":
    main()

