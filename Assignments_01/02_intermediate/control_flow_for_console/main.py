import random


def main():
  

    print("👋 Welcome to the High-Low Game!")
    print('--------------------------------')
    score = 0

    for i in range(1,6):
        print(f"Round {i}:")
        computer_num = random.randint(1,99)
        your_num = random.randint(1,99)
        if computer_num == your_num:
            your_num = random.randint(1,99)
        print(f'Your random number is {your_num}')
       
        choice = input("Do you think your number is higher or lower than computer's number?").strip().lower()
        if choice == "higher" and your_num > computer_num or choice=="lower" and your_num< computer_num:
            score += 1
            print("✅ You Are correct!")
            print(f"📍 Your score : {score}")
            print('--------------------------------')
        else:
            print(f"❌ Oop's incorrect. The computer's number was {computer_num}")
            print(f"📍 Your score : {score}")
            print('--------------------------------')


    print(f"😲 Your total score is {score}")
    print("🎉 Thank you for playing")     
   
   

if __name__=="__main__":
    main()