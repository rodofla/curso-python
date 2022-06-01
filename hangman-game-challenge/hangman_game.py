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
        By Rodrigo Flores"""


def display_hangman(tries):
    """
    It returns a string that is the ASCII art of the hangman
    
    :param tries: The number of tries the player has left
    :return: The list of hangman pictures.
    """
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
    """
    It clears the terminal screen
    """
    os.system('clear')


def get_word():
    """
    It opens the file, reads the file, splits the file into a list of words, and then chooses a random
    word from that list
    :return: A random word from the data.txt file
    """
    words = []
    with open("/home/rodofla/personalProjects/proyectos_cursos/curso-python/hangman-game-challenge/data.txt", "r", encoding="UTF-8") as f:
        words = f.read()
        random_word = random.choice(words.split()) 
    return random_word.upper()


def replace():
    """
    It takes a word, replaces all the accented vowels with their unaccented counterparts, and returns
    the new word
    :return: The word is being returned.
    """
    word = get_word()
    word = word.replace("Á", "A")
    word = word.replace("É", "E")
    word = word.replace("Í", "I")
    word = word.replace("Ó", "O")
    word = word.replace("Ú", "U")
    return word


def play(word):
    """
    The function play() takes a word as an argument and then runs a game of hangman with the user
    
    :param word: the word to be guessed
    """
    word_completion = "_" * len(word)
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
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion= "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        clear()
        print(SMALL_TITLE)
        print(display_hangman(tries))
        print(word_completion)
        print("\n")            
    if guessed:
        print("Congrats, you guessed the word! You win")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def run():
    get_word()
    replace()
    play(replace())


if __name__ == '__main__':
    run()