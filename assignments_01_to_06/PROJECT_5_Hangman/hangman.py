import random
import string
from words import words  # Ensure words.py contains a list named "words"

def get_valid_word(words):
    word = random.choice(words).upper()  # Convert word to uppercase
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()  # Ensure word remains uppercase
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word (uppercase now)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have " , lives, " lives left and you have used these letters:", " ".join(sorted(used_letters)))
        
        # Show current word with blanks
        word_list = [letter if letter in used_letters else "--" for letter in word]
        print("Current word:", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) # Remove guessed letter from set
            else:
                lives = lives - 1  # decrease one live if guessed incorectly
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died! sorry, the word was", word)
    if len(word_letters) == 0:
     print(f"\n🎉 Congratulations! You guessed the word: {word} 🎉")

# Run the game
hangman()
