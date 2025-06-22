#!/app/venv/bin/python
import random
import os


def clear_screen():
    """This function clear the screen in windows os environment"""
    if os.name == 'nt':
        os.system('cls')


WELCOME_SCREEN = "Welcome to the game Hangman"

HANGMAN_ASCII_ART = ("""
                  _    _ 
                 | |  | | 
                 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
                 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                 | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
                 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                                      __/ | 
                                     |___/ 
""")


HANGMAN_PHOTOS = {1: """    x-------x """,
                      2: """    x-------x
    |
    |
    |
    |
    |""",
                      3: """    x-------x
    |       |
    |       0
    |      
    |
    |""",
                      4: """    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |""",
                      5: """    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |""",
                      6: """    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |"""
                  }


def print_hangman(num_of_tries):
    """This function get an integer number_of_tries from 1 to 6 and returns the dictionary value for that number

    :param num_of_tries:
    :type: int
    :return:
    """

    return HANGMAN_PHOTOS[num_of_tries]


def check_win(secret_word, old_letters_guessed):
    """This function gets a secret word string and a list of letters guessed by the user and returns True of False
    if all letters in secret word string are in the list of letters guessed by the user

    :param secret_word: a string representing a word guessed by the user
    :type secret_word: str
    :param old_letters_guessed: a list of string characters
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """

    word = show_hidden_word(secret_word, old_letters_guessed)
    if word == ' '.join(secret_word):
        return True
    else:
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    """This function gets a secret word string and a list of letters guessed by the user and returns a string
    represents guessed and not guessed letters

    :param secret_word: a string representing a word guessed by the user
    :type secret_word: str
    :param old_letters_guessed: a list of string characters
    :type old_letters_guessed: list
    :return: string
    :rtype: str
    """

    index_counter = 0
    temp_string = ""
    for letter in secret_word:
        if letter.upper() in old_letters_guessed or letter.lower() in old_letters_guessed:
            temp_string += letter.lower()
        elif letter.upper() not in old_letters_guessed or letter.lower() not in old_letters_guessed:
            letter = "_"
            temp_string += letter.lower()
        index_counter += 1
    word = ' '.join(temp_string)
    return word


def check_valid_input(letter_guessed, old_letters_guessed):
    """This function gets 2 parameters a string and a list of guessed letters
    and returns boolean result for letter validity

    :param letter_guessed: a string representing the input
    :param old_letters_guessed: a list with guessed letters
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: boolean value for valid letter
    :rtype: boolean
    """

    if (len(letter_guessed) == 1 and letter_guessed.isalpha() and
        letter_guessed.lower() not in old_letters_guessed and
            letter_guessed.upper() not in old_letters_guessed):
        return True
    elif (len(letter_guessed) == 1 and letter_guessed.isalpha() and
          (letter_guessed.lower() in old_letters_guessed or
            letter_guessed.upper() in old_letters_guessed)):
        return False
    elif len(letter_guessed) == 1 and not letter_guessed.isalpha():
        print("X")
    elif len(letter_guessed) != 1 and not letter_guessed.isalpha():
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """This function gets 2 parameters a string and a list of guessed letters
    and returns boolean result for letter validity

    :param letter_guessed: a string representing the user input
    :param old_letters_guessed: a list with guessed letters
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: boolean value for valid letter
    :rtype: boolean
    """

    valid_input = check_valid_input(letter_guessed, old_letters_guessed)

    if valid_input is True:
        old_letters_guessed.append(letter_guessed.lower())
    elif valid_input is False:
        print("X")
        copy_of_list = old_letters_guessed.copy()
        print(sorted_list_items(copy_of_list))
    elif letter_guessed.lower() in old_letters_guessed or letter_guessed.upper() in old_letters_guessed:
        copy_of_list = old_letters_guessed.copy()
        print(sorted_list_items(copy_of_list))
    return valid_input


def choose_word(file_path, index):
    """This function gets a string as a path to a file and an index number variable as integer and returns
    a tuple with 1 item represnting the secret word chosen

    :param file_path
    :type string
    :param index
    :type integer
    :return: list_astuple : tuple with 1 items
    :rtype: list_astuple : tuple
    """

    newlist = []
    with open(file_path, "r") as file1:
        for line in file1:
            for word in line.split():
                newlist.append(word)

    secret_word = newlist[index % len(newlist) - 1]
    return (secret_word,)


def sorted_list_items(old_list_of_letters):
    """This function gets a list and copy it to a new list and returns all elements in the
    list ordered and separated as a string

    :param old_list_of_letters: a list representing user old letters already guessed
    :type old_list_of_letters: list
    :return: a string of sorted letters separated by ' -> '
    :rtype: str
    """

    old_list_of_letters.sort()
    return ' -> '.join(old_list_of_letters)


def main():
    # the number of false attempts the user tried so far initialize to 1
    num_of_tries = 1
    # the number of maximum false attempts the user can try
    MAX_TRIES = 6

    clear_screen()
    print("\n\t\t\t\t", WELCOME_SCREEN)
    print(HANGMAN_ASCII_ART)

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_filepath = os.path.join(script_dir, "words.txt")

    filepath = input(f"Enter file path [{default_filepath}]: ").strip()
    if not filepath:
        filepath = default_filepath

    index = input("Enter index: ")
    s_word = choose_word(filepath, int(index))
    print("\nLet's start\n")
    print(print_hangman(num_of_tries))

    secret_word = s_word[0]
    old_letters_guessed = []
    print(show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries < MAX_TRIES:
        guess_letter = input("Guess a letter: ")

        valid_guess = try_update_letter_guessed(guess_letter, old_letters_guessed)

        if valid_guess is True and (guess_letter.upper() in secret_word or guess_letter.lower() in secret_word):
            print(show_hidden_word(secret_word, old_letters_guessed))
        elif valid_guess is True and (guess_letter.upper() not in secret_word and guess_letter.lower() not in secret_word):
            num_of_tries += 1
            print(":(")
            print(print_hangman(num_of_tries), "\n")
            print(show_hidden_word(secret_word, old_letters_guessed))
        elif valid_guess is False:
            continue
        if check_win(secret_word, old_letters_guessed) is True:
            show_hidden_word(secret_word, old_letters_guessed)
            print("\n\033[1;32;12mWIN")
            break
        if num_of_tries == 6:
            print("\n\033[1;31;12mLOSE")
            print("\033[1;37;12m The secret word is:\033[1;34;12m ", secret_word)


if __name__ == "__main__":
    main()
