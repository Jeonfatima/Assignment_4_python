"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

import random
num_sides = 6


def main():
 die1 = random.randint(1,num_sides)
 die2 = random.randint(1,num_sides)
 total : int  = die1 + die2

 print("Each dice have " + str(num_sides) +" sides")
 print("Die 1 rolls " + str(die1))
 print("Die 2 rolls "+ str(die2))
 print(f"Their sum is {total}")

if __name__ == "__main__":
 main()