import random
def play():
    print("Welcome to Rock-Paper-Scissors!")
    
    user = input("Enter your choice:\n's' for scissors\n'p' for paper\n'r' for rock\n").lower()
    computer = random.choice(["r", "s", "p"])

    choices = {'r': "Rock", 'p': "Paper", 's': "Scissors"}
    
    if user not in choices:
        print("Invalid choice! Please enter 'r', 'p', or 's'.")
        return  # Exit the function if input is invalid

    print(f"Computer chose: {choices[computer]}")
    
    if user == computer:
        print("It's a Tie!")
        return

    if is_win(user, computer):
        print("🎉 You won!")
    else:
        print("😢 You Lost!")


def is_win(player , opponent):
    #returns true f player wins
    #p>r,s>p,r>s

    if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') or(player == 'r' and opponent == 's') :
        return True

play()