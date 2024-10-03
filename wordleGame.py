# Tyler Mestery            10-3-2024
# Creating an accurate model of the Famous Game 'Wordle'!

# Importing random module, natural language toolkit library, and system module (+getting words)
import random
import sys
import nltk
nltk.download('words')
from nltk.corpus import words

def intro():
    print("\n>>> Wordle Game")
    print(">>> By: Tyler Mestery\n")

def instructions():
    print("""
\n  Instructions:
    -Guess the random word.
    -Do so by entering a 5 letter word.
    -You have 5 attempts to guess it correctly.
    -When you guess a correct letter it will add it to the place it falls in the word.
    -Try and beat your record, by getting it in fewer attempts.
    """)

def randomWord():
    #Gets a random word from the Library ()
    five_letter_words = [word.lower() for word in words.words() if len(word) == 5]
    # Randomly select a word
    random_word = random.choice(five_letter_words)
    word = random_word

def gameStart():
    # Starting with 5 lives
    lives = 5

    #Gets a random word from the Library ()
    five_letter_words = [word.lower() for word in words.words() if len(word) == 5]
    # Randomly select a word
    random_word = random.choice(five_letter_words)
    word = random_word
    developingGuess = '_' * len(word)
    print(developingGuess)
    
    while lives > 0:
        # Gets users lowercase, spaceless, and 5 letter guess 
        guess = input("Enter your word guess: ").strip().lower()
        while (len(guess) != 5):
            print("Enter a 5 letter guess!")
            guess = input("Enter your word guess: ")

        # Checks to see if guessed letters match actual words letters
        i = 0
        for chr in word:
            if chr == guess[i]:
                developingGuess = list(developingGuess)
                developingGuess[i] = guess[i]
                developingGuess = ''.join(developingGuess).strip()
                i += 1
        
        # Checks if the User Won the Game!
        if developingGuess == word:
            print(f"You Win!!! You correctly guessed the word '{word}' in only {(5-lives)} attempts!!\n")
            break

        # Checks if the User Lost the Game!
        if (developingGuess != word) and (lives == 1):
            print(f"You Lose!!! The correct word was {word}. Better luck next time!\n")
            break

        # Outputs the developing user guess, and live left
        print(f"{developingGuess}\n")
        lives -= 1
        print(f"\nYou have {lives} lives left!\n")

def main():
    intro()
    running = True

    while running:
        menu = input("Would you like to [p]lay, read [i]nstructions, or [q]uit?: ")
        while (menu != "p") and (menu != "i") and (menu != "q"):
            menu = input("Would you like to [p]lay, read [i]nstructions, or [q]uit?: ")
    
        if (menu == "p"):
            gameStart()
        if (menu == "i"):
            instructions()
        if (menu == "q"):
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()