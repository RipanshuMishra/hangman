import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pear", "peach", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 10

    print("Welcome to Hangman!")
    print("Guess fruit name only:")
    print("Guess the word: " + display_word(word, guessed_letters))

    while True:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("Incorrect guess. Attempts left:", attempts_left)
            print(hangman_stages[10 - attempts_left - 1])
            if attempts_left == 0:
                print("You ran out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break

if __name__ == "__main__":
    hangman_stages = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        '''
    ]
    hangman()
