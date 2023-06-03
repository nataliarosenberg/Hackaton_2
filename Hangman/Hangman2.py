import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

from words import word_list

def check_win(word, guessed_letters):
    for letter in word:
        if not letter in guessed_letters:
            return False
    return True


def print_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def main():
    chosen_word = random.choice(word_list)
    guessed_letters = []
    numattempts = 7
    i = 1
    while True:
        print(HANGMAN_PICS[i - 1])
        print_word(chosen_word, guessed_letters)
        if check_win(chosen_word, guessed_letters):
            print("You win!")
            return

        if i >= numattempts: break

        guess = input("Input a letter or the whole word: ").lower()
        if len(guess) > 1 and guess == chosen_word:
            print("You win!")
            return
        elif len(guess) > 1 and not guess == chosen_word:
            i += 1
            continue
        elif len(guess) == 1:
            if guess in chosen_word:
                guessed_letters.append(guess)
            else:
                i += 1

    print(f"The word was: {chosen_word}")


main()
