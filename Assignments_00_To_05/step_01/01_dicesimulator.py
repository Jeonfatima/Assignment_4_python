"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

import random
num_sides = 6

def roll_dice():
 die1 : int = random.randint(1,num_sides)
 die2 : int = random.randint(1,num_sides)
 total = die1 + die2
 print("Total is " + str(total))

def main():
 die1 : int = 10
 print("die1 at start of main() is" + str(die1))
 roll_dice()
 roll_dice()
 roll_dice()
 print("die1 in main() is " + str(die1))

if __name__=="__main__":
 main()
