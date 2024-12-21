# Imports


# Characters used by program:
# ▄ Dot, or "dit"
# ▄▄▄ Dash, or "dah", which is 3 times "dit"
# The three spaces are added at the end of each character once they are translated

# Constants
MORSE_CODE_DICT = {
    ' ': ' ', # a space is 7 spaces wide in International Morse code, minus 3 before the space, minus 3 after the space
    'a': '▄ ▄▄▄',
    'b': '▄▄▄ ▄ ▄ ▄',
    'c': '▄▄▄ ▄ ▄▄▄ ▄',
    'd': '▄▄▄ ▄ ▄',
    'e': '▄',
    'f': '▄ ▄ ▄▄▄ ▄',
    'g': '▄▄▄ ▄▄▄ ▄',
    'h': '▄ ▄ ▄ ▄',
    'i': '▄ ▄',
    'j': '▄ ▄▄▄ ▄▄▄ ▄▄▄',
    'k': '▄▄▄ ▄ ▄▄▄',
    'l': '▄ ▄▄▄ ▄ ▄',
    'm': '▄▄▄ ▄▄▄',
    'n': '▄▄▄ ▄',
    'o': '▄▄▄ ▄▄▄ ▄▄▄',
    'p': '▄ ▄▄▄ ▄▄▄ ▄',
    'q': '▄▄▄ ▄▄▄ ▄ ▄▄▄',
    'r': '▄ ▄▄▄ ▄',
    's': '▄ ▄ ▄',
    't': '▄▄▄',
    'u': '▄ ▄ ▄▄▄',
    'v': '▄ ▄ ▄ ▄▄▄',
    'w': '▄ ▄▄▄ ▄▄▄',
    'x': '▄▄▄ ▄ ▄ ▄▄▄',
    'y': '▄▄▄ ▄ ▄▄▄ ▄▄▄',
    'z': '▄▄▄ ▄▄▄ ▄ ▄',
    '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
    '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄',
    '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄',
    '4': '▄ ▄ ▄ ▄ ▄▄▄',
    '5': '▄ ▄ ▄ ▄ ▄',
    '6': '▄▄▄ ▄ ▄ ▄ ▄',
    '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄',
    '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄',
    '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
    '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
}


# Functions
def greet_user() -> None:
    print('''
   _____                _       __  __                        _____          _      
  / ____|              ( )     |  \\/  |                      / ____|        | |     
 | |     __ _ _ __ ___ |/ ___  | \\  / | ___  _ __ ___  ___  | |     ___   __| | ___ 
 | |    / _` | '_ ` _ \\  / __| | |\\/| |/ _ \\| '__/ __|/ _ \\ | |    / _ \\ / _` |/ _ \\
 | |___| (_| | | | | | | \\__ \\ | |  | | (_) | |  \\__ \\  __/ | |___| (_) | (_| |  __/
  \\_____\\__,_|_| |_| |_| |___/ |_| _|_|\\___/|_|  |___/\\___|  \\_____\\___/ \\__,_|\\___|
 |__   __|                | |     | | (_)             | |            | |            
    | |_ __ __ _ _ __  ___| | __ _| |_ _  ___  _ __   | |_ ___   ___ | |            
    | | '__/ _` | '_ \\/ __| |/ _` | __| |/ _ \\| '_ \\  | __/ _ \\ / _ \\| |            
    | | | | (_| | | | \\__ \\ | (_| | |_| | (_) | | | | | || (_) | (_) | |            
    |_|_|  \\__,_|_| |_|___/_|\\__,_|\\__|_|\\___/|_| |_|  \\__\\___/ \\___/|_|            
                                                                                    
                                                                                    ''')


def translate_one_char(character: str) -> str:
    # Replaces every character that is not in alphabet with a space
    if character not in MORSE_CODE_DICT:
        return str(MORSE_CODE_DICT[' '])
    else:
        return str(MORSE_CODE_DICT[character])


def print_translated_text(query: str, result: str) -> None:
    print(f'Here is the translation for \n \"{query}\":')
    print(result)


def choose_to_continue() -> bool:
    choice = input("Do you want to continue? [Y/N]: ").lower()
    print()
    return choice == 'y'


def main() -> None:
    # Greet the user, explain quickly how program works
    greet_user()
    choice_to_continue = True

    while choice_to_continue:
        result = ''

        # Prompt a short text of a few words, store in variable as lower case
        text_to_translate = input('Please enter the text you want to translate into Morse code and press Enter: ').lower()

        # Using a dictionary, for each character (index), find the value associated in Morse code
        for character in text_to_translate:
            translated_char = translate_one_char(character)
            # Append that value to a result list
            result = result + translated_char
            result = result + "   "  # Adding three spaces at the end of each character

        # Once loop over, show that result list
        print_translated_text(text_to_translate, str(result))

        # Ask user if they want to continue or leave
        choice_to_continue = choose_to_continue()

    print("Thank you for using my translation tool. "
          "Don't hesitate to write me a review at sieger.camille@gmail.com")


if __name__ == '__main__':
    main()
