from curses.ascii import isalpha
import os #To clear screen
import random 

# ------------- Sprites:
HANGMAN_TITLE = """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    by Rodrigo Flores"""

SMALL_TITLE = """
█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
"""


def display_hangman(tries):
    HANGMAN_PICS = ['''  
                        +---+
                        |   |
                            |
                            |
                            |
                            |
                        =========''', '''  

                        +---+
                        |   |
                        O   |
                            |
                            |
                            |
                        =========''', '''  

                        +---+
                        |   |
                        O   |
                        |   |
                            |
                            |
                        =========''', '''  

                        +---+
                        |   |
                        O   |
                       /|   |
                            |
                            |
                        =========''', '''  

                        +---+
                        |   |
                        O   |
                       /|\  |
                            |
                            |
                        =========''', '''  

                        +---+
                        |   |
                        O   |
                       /|\  |
                       /    |
                            |
                        =========''', '''  

                        +---+
                        |   |
                        O   |
                       /|\  |
                       / \  |
                            |
                        =========''']
    return HANGMAN_PICS[tries]

def clear():
    os.system('clear')


def get_word():
    words = []
    with open("hangman-game-challenge/data.txt", "r", encoding="UTF-8") as f:
        words = f.read()
        random_word = random.choice(words.split())
    return random_word.upper()


def play(random_word):
    word_completion = "_" * len(random_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(HANGMAN_TITLE)
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in random_word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(random_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion= "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(random_word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != random_word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = random_word
        else:
            print("Not a valid guess.")
        clear()
        print(HANGMAN_TITLE)
        print(display_hangman(tries))
        print(word_completion)
        print("\n")            
    if guessed:
        print("Congrats, you guessed the word! You win")
    else:
        print("Sorry, you ran out of tries. The word was " + random_word + ". Maybe next time!")

def run():
    get_word()
    play(random_word=get_word())


if __name__ == '__main__':
    run()