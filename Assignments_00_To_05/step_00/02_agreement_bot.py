"""
program : Ageement bot
----------------------------
Take input animal from user and agree with the user on output
"""

def main():
    animal: str = input("What is your favourite animal? ")
    print(f"My favourite animal is also \033[1m{animal}\033[0m !")


if __name__ == "__main__":
    main()