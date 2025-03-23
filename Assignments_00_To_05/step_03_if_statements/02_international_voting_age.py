"""Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua."""

peturksbouipo_age : int = 16
stanlau_age : int = 25
mayengua_age : int = 48

def main():
    user_age = int(input("Enter your age: "))
     
    print("\nYour voting eligibility:\n ")

    if user_age >= peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where voting age is {peturksbouipo_age} .")
    else:
        print(f"You cannot vote in Peturksbouipo where voting age is {peturksbouipo_age} .")

    if user_age >= stanlau_age:
        print(f"You can vote in Stanlau where voting age is {stanlau_age} .")
    else:
        print(f"You cannot vote in Stanlau where voting age is {stanlau_age} .")

    if user_age >= mayengua_age:
        print(f"You can vote in Meyangua where voting age is {mayengua_age} .")
    else:
        print(f"You cannot vote in Meyangua where voting age is {mayengua_age} .")

if __name__=="__main__":
    main()

      