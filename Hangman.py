import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def game(word):
    word_completion = "_" *len(word)
    quessed = False
    quessed_letters = []
    gueassed_word = []
    tries = 6
    print('Start game Hangman!')
    print(display_hangman(tires))
    print(word_completion)
    print("\n")
    while not quessed and tries >0:
        quess = input('Please quess a word or letter: ').upper()
        if len(quess) == 1 and quess.isalpha():
            if quess in quessed_letters:
                print('You already quessed the letter', quess)
            elif quess not in quessed_letters:
                print(quess, 'is not in the word.')
                tries -=1
                quessed_letters.append(quess)
            else:
                print('Good job', quess, 'is in the word!')
                quessed_letters.append(quess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word)if letter == quess]
                for index in indices:
                    word_as_list[index] = quess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    quessed = True
        elif len(quess)==len(word) and quess.isalpha():
                if quess in quessed_letters:
                    print('You already quessed the word', quess)
                elif quess !=word:
                    print(quess, "is not the word.")
                    tries -= 1
                    quessed_words.append(quess)
                else:
                    quessed = True
                    word_completion = word
        else:
            print('Not a valid quess.')
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
if quessed:
    print("Congrats, you quessed the word! You win!")
else:
    print('sorry you lost.')
def display_hangman(tries):
    stages =['''
  3.       +----+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.       +----+
  9.       |    0
 10.       |
 11.       |
 12.      ===''', '''
 13.       +----+
 14.       |    0
 15.       |    |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']
    return stages[tries]
def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == __main__:
    main()


